"""Table Internet-I point/range conventions, without month-start safety buffers."""
import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay

# Explicit calendar proxy, not an assertion of complete historical exchange rules.
BUSINESS_DAY = CustomBusinessDay(calendar=USFederalHolidayCalendar())
PREVIOUS_LAST = {'LBR','C','O','RR','S','SM','BO','W','NG','HG','GC','PA','PL','SI'}


def notice_convention(code, delivery_month, range_endpoint='first'):
    if pd.isna(delivery_month):
        return pd.NaT, 'missing_delivery_month'
    month = pd.Timestamp(delivery_month).replace(day=1)
    first = BUSINESS_DAY.rollforward(month)
    if code in PREVIOUS_LAST:
        return BUSINESS_DAY.rollback(month-pd.Timedelta(days=1)), 'last_business_day_previous_month'
    if code in {'CC','KC'}:
        return first-(10 if code=='CC' else 7)*BUSINESS_DAY, 'business_days_before_first_business_day'
    if code in {'CT','LB'}:
        return month+pd.Timedelta(days=14), 'approximately_day_15'
    if code in {'OJ','SB'}:
        return first, 'first_business_day'
    if code=='CL':
        return month-pd.offsets.MonthBegin(1)+pd.Timedelta(days=24), 'approximately_previous_month_day_25'
    if code in {'HO','PN','RB','HU'}:
        return first+(0 if range_endpoint=='first' else 1)*BUSINESS_DAY, 'business_day_range_1_to_2'
    if code in {'LC','PB'}:
        return month+pd.Timedelta(days=3 if range_endpoint=='first' else 9), 'calendar_day_range_4_to_10'
    if code=='FC':
        end=month+pd.offsets.MonthEnd(0)
        return end-pd.Timedelta(days=(end.weekday()-3)%7), 'cash_settled_last_thursday'
    if code=='LH':
        return month+pd.Timedelta(days=9), 'cash_settled_approximately_day_10'
    return pd.NaT, 'unresolved'
