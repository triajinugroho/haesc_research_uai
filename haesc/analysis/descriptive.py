"""Descriptive statistics utilities for HAESC survey data."""
from __future__ import annotations
import pandas as pd
import numpy as np


class DescriptiveStats:
    """Compute and format descriptive statistics for survey data."""

    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df

    def summary(self, cols: list[str] | None = None) -> pd.DataFrame:
        """Return mean, std, min, max, skewness, kurtosis for each item."""
        data = self.df[cols] if cols else self.df
        stats = data.agg(["mean", "std", "min", "max", "skew"]).T
        stats["kurtosis"] = data.kurtosis()
        stats.columns = ["Mean", "SD", "Min", "Max", "Skewness", "Kurtosis"]
        return stats.round(3)

    def frequency_table(self, col: str) -> pd.DataFrame:
        counts = self.df[col].value_counts().sort_index()
        freq = pd.DataFrame({
            "Frequency": counts,
            "Percent": (counts / len(self.df) * 100).round(1),
            "Cumulative %": (counts / len(self.df) * 100).cumsum().round(1),
        })
        return freq

    def construct_means(self, construct_map: dict[str, list[str]]) -> pd.DataFrame:
        """Return mean score per construct given a mapping of construct → indicator list."""
        rows = {}
        for construct, indicators in construct_map.items():
            available = [i for i in indicators if i in self.df.columns]
            if not available:
                continue
            scores = self.df[available].mean(axis=1)
            rows[construct] = {
                "N": len(scores),
                "Mean": round(scores.mean(), 3),
                "SD": round(scores.std(), 3),
                "Min": round(scores.min(), 3),
                "Max": round(scores.max(), 3),
            }
        return pd.DataFrame(rows).T

    @staticmethod
    def interpret_mean(mean: float, scale_max: int = 5) -> str:
        thresholds = [
            (scale_max * 0.20, "Very Low"),
            (scale_max * 0.40, "Low"),
            (scale_max * 0.60, "Moderate"),
            (scale_max * 0.80, "High"),
            (scale_max * 1.00, "Very High"),
        ]
        for threshold, label in thresholds:
            if mean <= threshold:
                return label
        return "Very High"
