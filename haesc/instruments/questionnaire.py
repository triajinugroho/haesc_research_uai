"""
HAESC Quantitative Survey Questionnaire
========================================
Likert 1–5 instrument covering all three constructs:
  X – HAESC (11 items)
  M – Brand Attachment (6 items)
  Y – Customer Satisfaction (6 items)
Total: 23 items + screening + demographics
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List

from haesc.model import HAESCModel, Indicator
from haesc.config import ResearchConfig


@dataclass
class Section:
    title: str
    title_id: str
    instructions: str
    instructions_id: str
    items: List[Indicator]


class Questionnaire:
    """Builds and exports the full survey instrument."""

    CFG = ResearchConfig()

    SCREENING_ITEMS: List[dict] = [
        {
            "code": "S1",
            "text_id": "Apakah Anda pernah membeli produk busana Muslim secara online dalam 6 bulan terakhir?",
            "text_en": "Have you purchased Muslim fashion products online in the past 6 months?",
            "type": "yes_no",
            "disqualify_on": "Tidak / No",
        },
        {
            "code": "S2",
            "text_id": "Apakah Anda pernah berinteraksi dengan layanan pelanggan (chatbot atau agen manusia) dari merek busana Muslim?",
            "text_en": "Have you interacted with customer service (chatbot or human agent) from a Muslim fashion brand?",
            "type": "yes_no",
            "disqualify_on": "Tidak / No",
        },
    ]

    DEMOGRAPHIC_ITEMS: List[dict] = [
        {"code": "D1", "text_id": "Usia", "text_en": "Age",
         "type": "multiple_choice",
         "options": ["< 18", "18–24", "25–34", "35–44", "45–54", "≥ 55"]},
        {"code": "D2", "text_id": "Jenis Kelamin", "text_en": "Gender",
         "type": "multiple_choice",
         "options": ["Laki-laki / Male", "Perempuan / Female", "Lainnya / Other", "Tidak ingin menyebutkan / Prefer not to say"]},
        {"code": "D3", "text_id": "Kota Domisili", "text_en": "City of Residence",
         "type": "multiple_choice",
         "options": ["Jakarta", "Bandung", "Yogyakarta", "Surabaya", "Bali", "Lainnya / Other"]},
        {"code": "D4", "text_id": "Pendidikan Terakhir", "text_en": "Highest Education",
         "type": "multiple_choice",
         "options": ["SMA/SMK", "Diploma", "S1/Sarjana", "S2/Magister", "S3/Doktor", "Lainnya"]},
        {"code": "D5", "text_id": "Frekuensi Berbelanja Busana Muslim Online (per tahun)",
         "text_en": "Frequency of Online Muslim Fashion Shopping (per year)",
         "type": "multiple_choice",
         "options": ["1–2 kali", "3–5 kali", "6–10 kali", "> 10 kali"]},
        {"code": "D6", "text_id": "Jenis Interaksi Layanan Terakhir",
         "text_en": "Type of Last Service Interaction",
         "type": "multiple_choice",
         "options": ["Chatbot / AI otomatis", "Agen manusia", "Keduanya (AI lalu manusia)", "Tidak yakin"]},
    ]

    def __init__(self) -> None:
        self._model = HAESCModel()
        self._sections = self._build_sections()

    def _build_sections(self) -> List[Section]:
        return [
            Section(
                title="Part A: Human-AI Empathic Service Communication (HAESC)",
                title_id="Bagian A: Komunikasi Layanan Empatik Manusia-AI (HAESC)",
                instructions=(
                    "The following statements relate to your experience communicating "
                    "with the customer service of a Muslim fashion brand "
                    "(whether through a chatbot, human agent, or both). "
                    "Please rate each statement on a scale of 1 (Strongly Disagree) "
                    "to 5 (Strongly Agree)."
                ),
                instructions_id=(
                    "Pernyataan-pernyataan berikut berkaitan dengan pengalaman Anda "
                    "berkomunikasi dengan layanan pelanggan merek busana Muslim "
                    "(baik melalui chatbot, agen manusia, atau keduanya). "
                    "Nilailah setiap pernyataan pada skala 1 (Sangat Tidak Setuju) "
                    "hingga 5 (Sangat Setuju)."
                ),
                items=HAESCModel.indicators_by_construct("X"),
            ),
            Section(
                title="Part B: Brand Attachment",
                title_id="Bagian B: Kelekatan Merek",
                instructions=(
                    "Please rate the following statements about your feelings "
                    "towards the Muslim fashion brand you most recently interacted with."
                ),
                instructions_id=(
                    "Nilailah pernyataan-pernyataan berikut tentang perasaan Anda "
                    "terhadap merek busana Muslim yang paling baru Anda interaksikan."
                ),
                items=HAESCModel.indicators_by_construct("M"),
            ),
            Section(
                title="Part C: Customer Satisfaction",
                title_id="Bagian C: Kepuasan Pelanggan",
                instructions=(
                    "Please rate the following statements about your overall "
                    "satisfaction with the service experience."
                ),
                instructions_id=(
                    "Nilailah pernyataan-pernyataan berikut tentang kepuasan "
                    "Anda secara keseluruhan terhadap pengalaman layanan tersebut."
                ),
                items=HAESCModel.indicators_by_construct("Y"),
            ),
        ]

    @property
    def sections(self) -> List[Section]:
        return self._sections

    @property
    def total_items(self) -> int:
        return sum(len(s.items) for s in self._sections)

    def to_dict(self) -> dict:
        return {
            "title": "HAESC Research Survey",
            "title_id": "Survei Penelitian HAESC",
            "screening": self.SCREENING_ITEMS,
            "demographics": self.DEMOGRAPHIC_ITEMS,
            "sections": [
                {
                    "title": s.title,
                    "title_id": s.title_id,
                    "instructions": s.instructions,
                    "instructions_id": s.instructions_id,
                    "items": [
                        {
                            "code": item.code,
                            "text_en": item.text_en,
                            "text_id": item.text_id,
                            "dimension": item.dimension,
                            "construct": item.construct,
                            "scale": {"min": 1, "max": 5, "labels": ResearchConfig().scale_labels},
                        }
                        for item in s.items
                    ],
                }
                for s in self._sections
            ],
            "total_items": self.total_items,
        }

    def print_full(self, lang: str = "id") -> None:
        """Print the full questionnaire. lang='id' for Indonesian, 'en' for English."""
        attr_title = "title_id" if lang == "id" else "title"
        attr_text = "text_id" if lang == "id" else "text_en"
        attr_inst = "instructions_id" if lang == "id" else "instructions"

        print("=" * 70)
        print("KUESIONER PENELITIAN HAESC" if lang == "id" else "HAESC RESEARCH QUESTIONNAIRE")
        print("Universitas Al Azhar Indonesia – 2026")
        print("=" * 70)

        print("\n--- SKRINING / SCREENING ---")
        for item in self.SCREENING_ITEMS:
            print(f"  [{item['code']}] {item[attr_text]}")

        print("\n--- DEMOGRAFI / DEMOGRAPHICS ---")
        for item in self.DEMOGRAPHIC_ITEMS:
            print(f"  [{item['code']}] {item[attr_text]}")
            for opt in item.get("options", []):
                print(f"        ○ {opt}")

        for section in self._sections:
            print(f"\n{'=' * 70}")
            print(getattr(section, attr_title))
            print(getattr(section, attr_inst))
            print()
            for item in section.items:
                print(f"  [{item.code}] {getattr(item, attr_text)}")
                print(f"        1=STS  2=TS  3=N  4=S  5=SS")
        print("=" * 70)
        print(f"Total item pengukuran: {self.total_items}")
