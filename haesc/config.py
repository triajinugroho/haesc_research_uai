"""Research configuration constants."""
from dataclasses import dataclass, field
from typing import List


@dataclass(frozen=True)
class ResearchConfig:
    # Sample design
    population_size: int = 2670
    sample_size: int = 267
    sampling_method: str = "purposive"
    cities: List[str] = field(default_factory=lambda: [
        "Jakarta", "Bandung", "Yogyakarta", "Surabaya", "Bali"
    ])
    respondents_per_city: int = 54  # ~267 / 5

    # Eligibility
    min_purchase_recency_months: int = 6
    product_category: str = "Muslim fashion"

    # Qualitative sample
    service_managers_n: int = 10
    customers_qual_n: int = 5
    ai_specialists_n: int = 2

    # SEM-PLS thresholds
    min_outer_loading: float = 0.70
    min_ave: float = 0.50
    max_htmt: float = 0.85
    min_cr: float = 0.70
    min_cronbach_alpha: float = 0.70
    significance_level: float = 0.05
    bootstrap_samples: int = 5000

    # Likert scale
    scale_min: int = 1
    scale_max: int = 5
    scale_labels: List[str] = field(default_factory=lambda: [
        "Sangat Tidak Setuju",
        "Tidak Setuju",
        "Netral",
        "Setuju",
        "Sangat Setuju",
    ])

    # Target publication
    target_journal: str = "Human-Machine Communication"
    target_quartile: str = "Scopus Q1"
