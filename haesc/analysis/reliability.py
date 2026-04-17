"""
Reliability and validity analysis for HAESC measurement model.

Covers:
  - Cronbach's Alpha
  - Composite Reliability (CR)
  - Average Variance Extracted (AVE)
  - HTMT discriminant validity check
"""
from __future__ import annotations
import numpy as np
import pandas as pd
from haesc.config import ResearchConfig


CFG = ResearchConfig()


def cronbach_alpha(data: pd.DataFrame) -> float:
    """Compute Cronbach's Alpha for the columns in data."""
    k = data.shape[1]
    if k < 2:
        return np.nan
    item_var = data.var(axis=0, ddof=1).sum()
    total_var = data.sum(axis=1).var(ddof=1)
    return (k / (k - 1)) * (1 - item_var / total_var)


def composite_reliability(loadings: np.ndarray) -> float:
    """Compute CR from an array of outer loadings."""
    sum_lam = loadings.sum()
    sum_err = (1 - loadings ** 2).sum()
    return (sum_lam ** 2) / (sum_lam ** 2 + sum_err)


def ave(loadings: np.ndarray) -> float:
    """Compute Average Variance Extracted from outer loadings."""
    return (loadings ** 2).mean()


def htmt(
    construct_a: pd.DataFrame,
    construct_b: pd.DataFrame,
) -> float:
    """
    Compute HTMT ratio between two constructs.
    construct_a, construct_b: DataFrames of indicator columns.
    """
    corr_matrix = pd.concat([construct_a, construct_b], axis=1).corr()
    a_cols = construct_a.columns.tolist()
    b_cols = construct_b.columns.tolist()
    cross = corr_matrix.loc[a_cols, b_cols].values
    aa = corr_matrix.loc[a_cols, a_cols].values
    bb = corr_matrix.loc[b_cols, b_cols].values

    mean_cross = np.abs(cross).mean()
    n_a = len(a_cols)
    n_b = len(b_cols)
    mean_aa = aa[np.triu_indices(n_a, k=1)].mean() if n_a > 1 else 1.0
    mean_bb = bb[np.triu_indices(n_b, k=1)].mean() if n_b > 1 else 1.0
    return mean_cross / np.sqrt(mean_aa * mean_bb)


class ReliabilityAnalysis:
    """Run full measurement model quality assessment."""

    THRESHOLDS = {
        "cronbach_alpha": CFG.min_cronbach_alpha,
        "cr": CFG.min_cr,
        "ave": CFG.min_ave,
        "htmt": CFG.max_htmt,
        "outer_loading": CFG.min_outer_loading,
    }

    def __init__(
        self,
        df: pd.DataFrame,
        construct_indicator_map: dict[str, list[str]],
    ) -> None:
        self.df = df
        self.map = construct_indicator_map

    def run(self) -> pd.DataFrame:
        rows = []
        for construct, indicators in self.map.items():
            cols = [i for i in indicators if i in self.df.columns]
            if not cols:
                continue
            data = self.df[cols].dropna()
            alpha = cronbach_alpha(data)
            loadings = data.corrwith(data.mean(axis=1)).values
            cr = composite_reliability(loadings)
            avg_var = ave(loadings)
            rows.append({
                "Construct": construct,
                "Items": len(cols),
                "Cronbach_Alpha": round(alpha, 3),
                "CR": round(cr, 3),
                "AVE": round(avg_var, 3),
                "Alpha_OK": alpha >= self.THRESHOLDS["cronbach_alpha"],
                "CR_OK": cr >= self.THRESHOLDS["cr"],
                "AVE_OK": avg_var >= self.THRESHOLDS["ave"],
            })
        return pd.DataFrame(rows).set_index("Construct")
