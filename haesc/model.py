"""
HAESC Research Model
====================
Defines all constructs, dimensions, indicators, and hypotheses for the
Human-AI Empathic Service Communication (HAESC) structural model.
"""
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Tuple


class ConstructType(str, Enum):
    INDEPENDENT = "independent"
    MEDIATING = "mediating"
    DEPENDENT = "dependent"


@dataclass
class Indicator:
    code: str
    text_id: str          # Indonesian wording
    text_en: str          # English translation
    dimension: str
    construct: str


@dataclass
class Construct:
    name: str
    code: str
    construct_type: ConstructType
    dimensions: List[str]
    indicators: List[Indicator] = field(default_factory=list)

    def indicators_for_dimension(self, dimension: str) -> List[Indicator]:
        return [i for i in self.indicators if i.dimension == dimension]


@dataclass
class Hypothesis:
    code: str
    description: str
    from_construct: str
    to_construct: str
    via: str | None = None

    def __str__(self) -> str:
        if self.via:
            return f"{self.code}: {self.from_construct} → {self.to_construct} (via {self.via})"
        return f"{self.code}: {self.from_construct} → {self.to_construct}"


class HAESCModel:
    """
    Full structural model for the HAESC research.

    Independent Variable (X):  HAESC – Human-AI Empathic Service Communication
    Mediating Variable  (M):   Brand Attachment
    Dependent Variable  (Y):   Customer Satisfaction
    """

    # ------------------------------------------------------------------ #
    #  Constructs                                                          #
    # ------------------------------------------------------------------ #
    CONSTRUCTS: Dict[str, Construct] = {
        "X": Construct(
            name="Human-AI Empathic Service Communication (HAESC)",
            code="X",
            construct_type=ConstructType.INDEPENDENT,
            dimensions=[
                "Service Communication",
                "Perceived Interactional Empathy",
                "Relational Trust",
            ],
        ),
        "M": Construct(
            name="Brand Attachment",
            code="M",
            construct_type=ConstructType.MEDIATING,
            dimensions=[
                "Emotional Connection",
                "Brand Affection",
                "Brand Passion",
            ],
        ),
        "Y": Construct(
            name="Customer Satisfaction",
            code="Y",
            construct_type=ConstructType.DEPENDENT,
            dimensions=[
                "Overall Satisfaction",
                "Expectation Confirmation",
                "Satisfaction with Problem Resolution",
            ],
        ),
    }

    # ------------------------------------------------------------------ #
    #  Indicators                                                          #
    # ------------------------------------------------------------------ #
    INDICATORS: List[Indicator] = [
        # --- X: Service Communication ---
        Indicator("SC1", "Layanan merespons pertanyaan saya dengan cepat dan tepat.",
                  "The service responded to my enquiries quickly and accurately.",
                  "Service Communication", "X"),
        Indicator("SC2", "Komunikasi layanan disesuaikan dengan kebutuhan personal saya.",
                  "Service communication was personalised to my individual needs.",
                  "Service Communication", "X"),
        Indicator("SC3", "Nada komunikasi layanan terasa sesuai dan sopan.",
                  "The tone of service communication felt appropriate and polite.",
                  "Service Communication", "X"),
        Indicator("SC4", "Layanan menunjukkan kepekaan terhadap nilai budaya saya.",
                  "The service demonstrated sensitivity to my cultural values.",
                  "Service Communication", "X"),
        Indicator("SC5", "Peralihan antara agen AI dan manusia berlangsung mulus.",
                  "The transition between AI and human agents was seamless.",
                  "Service Communication", "X"),

        # --- X: Perceived Interactional Empathy ---
        Indicator("PIE1", "Layanan memahami perasaan saya selama interaksi.",
                  "The service understood my feelings during the interaction.",
                  "Perceived Interactional Empathy", "X"),
        Indicator("PIE2", "Layanan memahami perspektif dan situasi saya.",
                  "The service understood my perspective and situation.",
                  "Perceived Interactional Empathy", "X"),
        Indicator("PIE3", "Respons layanan menunjukkan kepedulian yang tulus terhadap masalah saya.",
                  "Service responses showed genuine concern for my concerns.",
                  "Perceived Interactional Empathy", "X"),

        # --- X: Relational Trust ---
        Indicator("RT1", "Saya yakin layanan memberikan informasi yang jujur.",
                  "I believe the service provides honest information.",
                  "Relational Trust", "X"),
        Indicator("RT2", "Layanan konsisten dan dapat diandalkan.",
                  "The service is consistent and reliable.",
                  "Relational Trust", "X"),
        Indicator("RT3", "Saya percaya layanan bertindak demi kepentingan terbaik saya.",
                  "I trust that the service acts in my best interests.",
                  "Relational Trust", "X"),

        # --- M: Emotional Connection ---
        Indicator("EC1", "Saya merasa terhubung secara emosional dengan merek ini.",
                  "I feel emotionally connected to this brand.",
                  "Emotional Connection", "M"),
        Indicator("EC2", "Merek ini terasa seperti bagian dari identitas saya.",
                  "This brand feels like part of my identity.",
                  "Emotional Connection", "M"),

        # --- M: Brand Affection ---
        Indicator("BA1", "Saya memiliki perasaan hangat terhadap merek ini.",
                  "I have warm feelings towards this brand.",
                  "Brand Affection", "M"),
        Indicator("BA2", "Merek ini membuat saya merasa nyaman dan dihargai.",
                  "This brand makes me feel comfortable and valued.",
                  "Brand Affection", "M"),

        # --- M: Brand Passion ---
        Indicator("BP1", "Saya sangat antusias dengan merek ini.",
                  "I am highly enthusiastic about this brand.",
                  "Brand Passion", "M"),
        Indicator("BP2", "Saya akan merekomendasikan merek ini kepada orang lain.",
                  "I would recommend this brand to others.",
                  "Brand Passion", "M"),

        # --- Y: Overall Satisfaction ---
        Indicator("OS1", "Secara keseluruhan, saya puas dengan pengalaman layanan.",
                  "Overall, I am satisfied with the service experience.",
                  "Overall Satisfaction", "Y"),
        Indicator("OS2", "Pengalaman layanan melebihi ekspektasi saya.",
                  "The service experience exceeded my expectations.",
                  "Overall Satisfaction", "Y"),

        # --- Y: Expectation Confirmation ---
        Indicator("EXC1", "Layanan yang saya terima sesuai dengan yang dijanjikan.",
                  "The service I received matched what was promised.",
                  "Expectation Confirmation", "Y"),
        Indicator("EXC2", "Kualitas layanan konsisten dengan reputasi merek.",
                  "Service quality was consistent with the brand's reputation.",
                  "Expectation Confirmation", "Y"),

        # --- Y: Satisfaction with Problem Resolution ---
        Indicator("PR1", "Keluhan atau masalah saya diselesaikan secara efektif.",
                  "My complaints or issues were resolved effectively.",
                  "Satisfaction with Problem Resolution", "Y"),
        Indicator("PR2", "Saya puas dengan cara layanan menangani masalah saya.",
                  "I was satisfied with how the service handled my problem.",
                  "Satisfaction with Problem Resolution", "Y"),
    ]

    # ------------------------------------------------------------------ #
    #  Hypotheses                                                          #
    # ------------------------------------------------------------------ #
    HYPOTHESES: List[Hypothesis] = [
        Hypothesis("H1", "HAESC positively affects Brand Attachment.",
                   "X", "M"),
        Hypothesis("H2", "HAESC positively affects Customer Satisfaction.",
                   "X", "Y"),
        Hypothesis("H3", "Brand Attachment positively affects Customer Satisfaction.",
                   "M", "Y"),
        Hypothesis("H4", "Brand Attachment mediates the effect of HAESC on Customer Satisfaction.",
                   "X", "Y", via="M"),
    ]

    # ------------------------------------------------------------------ #
    #  Structural paths                                                    #
    # ------------------------------------------------------------------ #
    STRUCTURAL_PATHS: List[Tuple[str, str]] = [
        ("X", "M"),
        ("X", "Y"),
        ("M", "Y"),
    ]

    @classmethod
    def all_indicators(cls) -> List[Indicator]:
        return cls.INDICATORS

    @classmethod
    def indicators_by_construct(cls, construct_code: str) -> List[Indicator]:
        return [i for i in cls.INDICATORS if i.construct == construct_code]

    @classmethod
    def summary(cls) -> str:
        lines = ["HAESC Research Model Summary", "=" * 40]
        for code, construct in cls.CONSTRUCTS.items():
            n_ind = len(cls.indicators_by_construct(code))
            lines.append(
                f"[{construct.construct_type.value.upper():12s}] {construct.name}"
                f"  ({len(construct.dimensions)} dimensions, {n_ind} indicators)"
            )
        lines.append("")
        lines.append("Hypotheses:")
        for h in cls.HYPOTHESES:
            lines.append(f"  {h}")
        return "\n".join(lines)
