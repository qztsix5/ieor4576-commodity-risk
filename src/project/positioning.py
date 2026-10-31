"""Release-aware positioning inputs. Never infer publication from report date."""
import pandas as pd


def align_releases(weekly,releases):
    if releases.report_date.duplicated().any(): raise ValueError('Duplicate release dates')
    d=weekly.merge(releases,on='report_date',how='left',validate='many_to_one')
    if d.release_date.isna().any(): raise ValueError('Incomplete official CFTC release calendar')
    if (d.release_date<d.report_date).any(): raise ValueError('Release before measurement')
    dates=pd.date_range(d.release_date.min(),d.release_date.max()+pd.offsets.MonthEnd(0),freq='ME')
    frames=[]
    for code,g in d.groupby('paper_code'):
        # If a backlog is released together, use the newest report available then.
        g=g.sort_values(['release_date','report_date']).drop_duplicates('release_date',keep='last')
        aligned=pd.merge_asof(pd.DataFrame({'date':dates}),g.sort_values('release_date'),
                              left_on='date',right_on='release_date',direction='backward')
        aligned['paper_code']=code
        aligned['report_age_days']=(aligned.date-aligned.report_date).dt.days
        aligned['delta_net_noncommercial_share']=aligned.net_noncommercial_share.diff()
        frames.append(aligned)
    return pd.concat(frames,ignore_index=True)
