"""
HAESC Research Package
======================
Human-Artificial Intelligence Empathic Service Communication (HAESC) model
development research for the Indonesian Muslim Fashion Industry.

Universitas Al Azhar Indonesia (UAI), 2026

Researchers:
  - Kussusanti (Lead, Communication Science)
  - Tri Aji Nugroho (Informatics Engineering / AI)
  - Ruvira Arindita (Communication Science / PR)
  - Safira Hasna (Communication Science / PR)
  - Khairunnisa Syarief (Communication Science, Master's)
"""

__version__ = "0.1.0"
__authors__ = [
    "Kussusanti",
    "Tri Aji Nugroho",
    "Ruvira Arindita",
    "Safira Hasna",
    "Khairunnisa Syarief",
]
__institution__ = "Universitas Al Azhar Indonesia"
__year__ = 2026

from haesc.model import HAESCModel
from haesc.config import ResearchConfig

__all__ = ["HAESCModel", "ResearchConfig"]
