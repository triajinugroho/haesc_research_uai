"""
SEM-PLS Analysis Report Generator
====================================
Produces standardised tables for SmartPLS 4 output interpretation
following Hair et al. (2022) guidelines for PLS-SEM.

Usage:
  report = SEMPLSReport.from_smartpls_csv("path/to/smartpls_output.csv")
  report.print_summary()
"""
from __future__ import annotations
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List

from haesc.config import ResearchConfig
from haesc.model import HAESCModel

CFG = ResearchConfig()


@dataclass
class PathResult:
    from_construct: str
    to_construct: str
    beta: float
    t_stat: float
    p_value: float
    ci_lower: float
    ci_upper: float
    hypothesis: str = ""

    @property
    def significant(self) -> bool:
        return self.p_value < CFG.significance_level

    @property
    def decision(self) -> str:
        return "Supported" if self.significant else "Not Supported"

    def __str__(self) -> str:
        return (
            f"{self.hypothesis:4s}  {self.from_construct} → {self.to_construct}"
            f"  β={self.beta:.3f}  t={self.t_stat:.3f}  p={self.p_value:.3f}"
            f"  [{self.ci_lower:.3f}, {self.ci_upper:.3f}]  {self.decision}"
        )


@dataclass
class MediationResult:
    indirect_effect: float
    t_stat: float
    p_value: float
    ci_lower: float
    ci_upper: float
    via: str = "Brand Attachment (M)"

    @property
    def significant(self) -> bool:
        return self.p_value < CFG.significance_level

    @property
    def mediation_type(self) -> str:
        return "Partial mediation" if self.significant else "No mediation"


@dataclass
class SEMPLSReport:
    """Container for SEM-PLS results tables."""

    path_results: List[PathResult] = field(default_factory=list)
    mediation_result: MediationResult | None = None
    r_squared: Dict[str, float] = field(default_factory=dict)
    q_squared: Dict[str, float] = field(default_factory=dict)
    f_squared: Dict[str, float] = field(default_factory=dict)

    # ------------------------------------------------------------------ #
    #  Constructors                                                        #
    # ------------------------------------------------------------------ #
    @classmethod
    def template(cls) -> "SEMPLSReport":
        """Return a blank template pre-populated with hypothesis codes."""
        paths = []
        hyp_map = {("X", "M"): "H1", ("X", "Y"): "H2", ("M", "Y"): "H3"}
        for (fr, to), hyp in hyp_map.items():
            paths.append(PathResult(fr, to, 0.0, 0.0, 1.0, 0.0, 0.0, hypothesis=hyp))
        return cls(
            path_results=paths,
            mediation_result=MediationResult(0.0, 0.0, 1.0, 0.0, 0.0),
            r_squared={"M": 0.0, "Y": 0.0},
            q_squared={"M": 0.0, "Y": 0.0},
            f_squared={"X->M": 0.0, "X->Y": 0.0, "M->Y": 0.0},
        )

    @classmethod
    def from_dict(cls, data: dict) -> "SEMPLSReport":
        paths = [PathResult(**p) for p in data.get("path_results", [])]
        med = data.get("mediation_result")
        mediation = MediationResult(**med) if med else None
        return cls(
            path_results=paths,
            mediation_result=mediation,
            r_squared=data.get("r_squared", {}),
            q_squared=data.get("q_squared", {}),
            f_squared=data.get("f_squared", {}),
        )

    @classmethod
    def from_json(cls, path: str | Path) -> "SEMPLSReport":
        with open(path) as f:
            return cls.from_dict(json.load(f))

    def to_json(self, path: str | Path) -> None:
        import dataclasses
        with open(path, "w") as f:
            json.dump(dataclasses.asdict(self), f, indent=2)

    # ------------------------------------------------------------------ #
    #  Reporting                                                           #
    # ------------------------------------------------------------------ #
    def print_summary(self) -> None:
        print("=" * 70)
        print("HAESC SEM-PLS RESULTS SUMMARY")
        print(f"Bootstrap samples: {CFG.bootstrap_samples}  |  α = {CFG.significance_level}")
        print("=" * 70)

        print("\nStructural Model – Path Coefficients (H1–H3):")
        print("-" * 70)
        print(f"{'Hyp':<5} {'Path':<25} {'β':>6} {'t':>7} {'p':>7} {'95% CI':<18} {'Decision'}")
        print("-" * 70)
        for pr in self.path_results:
            ci = f"[{pr.ci_lower:.3f}, {pr.ci_upper:.3f}]"
            path = f"{pr.from_construct} → {pr.to_construct}"
            print(f"{pr.hypothesis:<5} {path:<25} {pr.beta:>6.3f} {pr.t_stat:>7.3f} "
                  f"{pr.p_value:>7.3f} {ci:<18} {pr.decision}")

        if self.mediation_result:
            m = self.mediation_result
            print("\nMediation Analysis – H4 (X → M → Y):")
            print("-" * 50)
            ci = f"[{m.ci_lower:.3f}, {m.ci_upper:.3f}]"
            print(f"  Indirect effect: {m.indirect_effect:.3f}  t={m.t_stat:.3f}  "
                  f"p={m.p_value:.3f}  {ci}")
            print(f"  Verdict: {m.mediation_type}")

        print("\nModel Fit:")
        print("-" * 40)
        for construct, r2 in self.r_squared.items():
            q2 = self.q_squared.get(construct, float("nan"))
            strength = self._r2_strength(r2)
            print(f"  {construct}: R²={r2:.3f} ({strength})  Q²={q2:.3f}")

        print("\nEffect Sizes (f²):")
        for path, f2 in self.f_squared.items():
            print(f"  {path}: f²={f2:.3f}  ({self._f2_strength(f2)})")
        print("=" * 70)

    @staticmethod
    def _r2_strength(r2: float) -> str:
        if r2 >= 0.67:
            return "substantial"
        if r2 >= 0.33:
            return "moderate"
        if r2 >= 0.19:
            return "weak"
        return "very weak"

    @staticmethod
    def _f2_strength(f2: float) -> str:
        if f2 >= 0.35:
            return "large"
        if f2 >= 0.15:
            return "medium"
        if f2 >= 0.02:
            return "small"
        return "negligible"
