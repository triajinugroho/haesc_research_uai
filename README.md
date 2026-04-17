# HAESC Research – Universitas Al Azhar Indonesia

**Pengembangan Model HAESC (Human-Artificial Intelligence Empathic Service Communication) pada Industri Busana Muslim Indonesia**

> *Development of the HAESC Model for the Indonesian Muslim Fashion Industry*

---

## Overview

This repository is the research package for a **fundamental research project** investigating how empathic communication can be achieved in hybrid human-AI customer service environments, with a focus on the Indonesian Muslim fashion industry.

The project develops the **HAESC model**, a theoretical and empirical framework integrating:
- Human–Machine Communication (HMC) theory
- Empathic service communication
- Cultural communication in an Indonesian high-context setting
- Structural Equation Modelling with Partial Least Squares (SEM-PLS)

---

## Research Team

| Name | Role | Discipline |
|---|---|---|
| **Kussusanti** | Lead Researcher | Communication Science |
| **Tri Aji Nugroho** | Co-Researcher | Informatics Engineering / AI |
| **Ruvira Arindita** | Co-Researcher | Communication Science / PR |
| **Safira Hasna** | Co-Researcher | Communication Science / PR |
| **Khairunnisa Syarief** | Research Assistant | Communication Science (Master's) |

**Institution:** Universitas Al Azhar Indonesia (UAI)  
**Year:** 2026

---

## Research Model

```
X (HAESC)  ──H1──►  M (Brand Attachment)
     │                       │
     H2                      H3
     │                       │
     └─────────►  Y (Customer Satisfaction)
           H4: X → M → Y  (mediation)
```

### Constructs & Dimensions

| Construct | Type | Dimensions | Indicators |
|---|---|---|---|
| **X – HAESC** | Independent | Service Communication · Perceived Interactional Empathy · Relational Trust | 11 |
| **M – Brand Attachment** | Mediating | Emotional Connection · Brand Affection · Brand Passion | 6 |
| **Y – Customer Satisfaction** | Dependent | Overall Satisfaction · Expectation Confirmation · Problem Resolution | 6 |

### Hypotheses

| # | Path | Description |
|---|---|---|
| H1 | X → M | HAESC positively affects Brand Attachment |
| H2 | X → Y | HAESC positively affects Customer Satisfaction |
| H3 | M → Y | Brand Attachment positively affects Customer Satisfaction |
| H4 | X → M → Y | Brand Attachment mediates HAESC → Customer Satisfaction |

---

## Methodology

### Phase 1 – Qualitative (Sequential Exploratory)

| Participant | n | Purpose |
|---|---|---|
| Service managers / CS agents | 10 | Explore empathic communication practices |
| Customers | 5 | Understand customer perceptions |
| AI specialists | 2 | Technical & design perspectives |

**Analysis:** Thematic coding → HAESC dimension mapping → indicator generation

### Phase 2 – Quantitative Survey

| Parameter | Value |
|---|---|
| Sample size | 267 respondents |
| Sampling | Purposive |
| Cities | Jakarta · Bandung · Yogyakarta · Surabaya · Bali |
| Eligibility | Muslim fashion purchase within last 6 months |
| Instrument | 23-item Likert 1–5 scale (bilingual ID/EN) |
| Analysis | SEM-PLS (SmartPLS 4) |

---

## Repository Structure

```
haesc_research_uai/
│
├── haesc/                        # Python research package
│   ├── __init__.py
│   ├── model.py                  # Constructs, indicators, hypotheses
│   ├── config.py                 # Research constants & SEM-PLS thresholds
│   ├── instruments/
│   │   ├── questionnaire.py      # 23-item bilingual survey instrument
│   │   └── interview_guide.py    # Qualitative interview guides (3 variants)
│   └── analysis/
│       ├── descriptive.py        # Descriptive statistics utilities
│       ├── reliability.py        # Cronbach α, CR, AVE, HTMT
│       └── sem_pls.py            # SEM-PLS results report generator
│
├── data/
│   ├── codebook.json             # Variable codebook
│   ├── raw/                      # Raw survey / interview data (gitignored)
│   ├── processed/                # Cleaned datasets
│   └── qualitative/              # Interview transcripts / coding
│
├── outputs/
│   ├── figures/                  # Charts and path diagrams
│   ├── tables/                   # Statistical tables (CSV/XLSX)
│   └── reports/                  # Final analysis reports
│
├── notebooks/                    # Jupyter analysis notebooks
├── tests/                        # pytest unit tests
│   ├── test_model.py
│   └── test_questionnaire.py
│
├── pyproject.toml                # Package metadata & dependencies
└── Kussusanti_Substansi Proposal Penelitian Fundamental (2).pdf
```

---

## Installation

```bash
# Clone the repository
git clone https://github.com/triajinugroho/haesc_research_uai.git
cd haesc_research_uai

# Install in editable mode with dev dependencies
pip install -e ".[dev]"

# Optional: install notebook support
pip install -e ".[notebooks]"
```

---

## Quick Start

```python
from haesc.model import HAESCModel
from haesc.instruments.questionnaire import Questionnaire
from haesc.analysis.sem_pls import SEMPLSReport

# Inspect the research model
print(HAESCModel.summary())

# Print the full survey instrument (Indonesian)
q = Questionnaire()
q.print_full(lang="id")

# Load SEM-PLS results and print summary
report = SEMPLSReport.from_json("outputs/reports/sem_pls_results.json")
report.print_summary()
```

---

## SEM-PLS Quality Thresholds

| Metric | Minimum | Reference |
|---|---|---|
| Outer Loading | ≥ 0.70 | Hair et al. (2022) |
| AVE | ≥ 0.50 | Fornell & Larcker (1981) |
| Composite Reliability | ≥ 0.70 | Hair et al. (2022) |
| Cronbach's Alpha | ≥ 0.70 | Nunnally (1978) |
| HTMT | < 0.85 | Henseler et al. (2015) |
| Bootstrap samples | 5,000 | Hair et al. (2022) |

---

## Expected Outputs

1. **HAESC theoretical model** – operationalised dimensions and validated indicators
2. **Peer-reviewed article** – target journal: *Human-Machine Communication* (Scopus Q1)
3. **Measurement instrument** – validated bilingual (ID/EN) 23-item survey scale
4. **Practical guidelines** – for Muslim fashion brands implementing hybrid AI service

---

## Theoretical Foundations

- **Human-Machine Communication (HMC)** – Guzman (2018); Nass & Moon (2000) CASA
- **Theory of Interactive Media Effects (TIME)** – Valkenburg & Oliver (2020)
- **Empathic Communication in Service** – Hennig-Thurau et al. (2006)
- **High-Context Communication** – Hall (1976); Indonesian cultural adaptation

---

## SDG Alignment

This research contributes to **UN Sustainable Development Goal #8** – Decent Work and Economic Growth – by supporting the development of ethical, culturally intelligent AI in Indonesia's Muslim fashion industry.

---

## Running Tests

```bash
pytest tests/ -v
```

---

## License

MIT License – see [LICENSE](LICENSE) for details.

---

*Universitas Al Azhar Indonesia · Fakultas Ilmu Komunikasi · 2026*
