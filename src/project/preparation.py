"""Rebuild the data-stage artifacts without fitting pricing models."""
from .paths import ROOT, ensure_directories
from .data import build_dataset
from .auxiliary import download_public, prepare_public, download_equities, prepare_equities
from .acquisition import connect_wrds, download_futures
from .diagnostics import run_diagnostics
from .portfolios import make_portfolios


def prepare_data(download=False):
    ensure_directories()
    if download:
        conn=connect_wrds()
        try:
            download_futures(conn)
            download_equities(conn)
        finally:
            conn.close()
        download_public(1986,2025)
    p=build_dataset()
    f,w=make_portfolios(p)
    f.to_parquet(ROOT/'data/processed/portfolios.parquet')
    w.to_parquet(ROOT/'data/processed/weights.parquet',index=False)
    run_diagnostics(p,'main')
    from .diagnostics import overlap_validation
    overlap_validation(p)
    prepare_public()
    prepare_equities()
