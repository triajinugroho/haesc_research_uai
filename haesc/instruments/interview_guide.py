"""
Qualitative Interview Guides
==============================
Phase 1 of the sequential mixed-methods design.

Three guide variants:
  1. ServiceAgentGuide  – for customer service managers / CS agents
  2. CustomerGuide      – for customers with hybrid service experience
  3. AISpecialistGuide  – for AI engineers / chatbot developers
"""
from dataclasses import dataclass, field
from typing import List


@dataclass
class InterviewQuestion:
    code: str
    theme: str
    text_id: str
    text_en: str
    probes: List[str] = field(default_factory=list)


@dataclass
class InterviewGuide:
    target: str
    target_id: str
    objective: str
    duration_minutes: int
    questions: List[InterviewQuestion]


SERVICE_AGENT_GUIDE = InterviewGuide(
    target="Customer Service Managers / Agents",
    target_id="Manajer / Agen Layanan Pelanggan",
    objective=(
        "Explore how empathy is practiced in hybrid human-AI service "
        "communication within Indonesian Muslim fashion brands."
    ),
    duration_minutes=60,
    questions=[
        InterviewQuestion(
            "SA1", "Role & Context",
            "Bisakah Anda menceritakan peran Anda dan bagaimana layanan pelanggan bekerja di sini?",
            "Could you describe your role and how customer service operates here?",
            probes=["Sejak kapan menggunakan AI/chatbot?", "Bagaimana pembagian tugas antara AI dan manusia?"],
        ),
        InterviewQuestion(
            "SA2", "Empathic Communication Practice",
            "Bagaimana Anda memastikan komunikasi dengan pelanggan terasa empatik, baik melalui AI maupun agen manusia?",
            "How do you ensure customer communication feels empathic, whether via AI or human agents?",
            probes=["Contoh konkret?", "Tantangan utama?"],
        ),
        InterviewQuestion(
            "SA3", "Cultural Sensitivity",
            "Apakah ada penyesuaian khusus untuk konteks budaya Indonesia dalam layanan Anda?",
            "Are there specific cultural adaptations in your service for the Indonesian context?",
            probes=["Bahasa dan kesopanan?", "Nilai-nilai Islam?"],
        ),
        InterviewQuestion(
            "SA4", "AI Handoff",
            "Bagaimana proses peralihan dari chatbot ke agen manusia? Apa tantangannya?",
            "How does the handoff from chatbot to human agent work? What are the challenges?",
        ),
        InterviewQuestion(
            "SA5", "Customer Feedback",
            "Apa umpan balik pelanggan yang paling sering Anda terima tentang kualitas komunikasi layanan?",
            "What is the most common customer feedback you receive about service communication quality?",
        ),
        InterviewQuestion(
            "SA6", "Improvement",
            "Menurut Anda, apa yang paling perlu ditingkatkan dalam komunikasi layanan berbasis AI saat ini?",
            "In your view, what most needs improvement in current AI-based service communication?",
        ),
    ],
)

CUSTOMER_GUIDE = InterviewGuide(
    target="Customers with Hybrid Service Experience",
    target_id="Pelanggan dengan Pengalaman Layanan Hibrid",
    objective=(
        "Understand how customers perceive empathy and satisfaction "
        "in hybrid human-AI service interactions within Muslim fashion brands."
    ),
    duration_minutes=45,
    questions=[
        InterviewQuestion(
            "CG1", "Experience Description",
            "Bisakah Anda menceritakan pengalaman terakhir Anda menghubungi layanan pelanggan merek busana Muslim?",
            "Could you describe your most recent experience contacting a Muslim fashion brand's customer service?",
            probes=["Melalui platform apa?", "Jenis pertanyaan/keluhan apa?"],
        ),
        InterviewQuestion(
            "CG2", "Perceived Empathy",
            "Seberapa empatik menurut Anda respons yang Anda dapatkan? Apa yang membuat Anda merasakan hal itu?",
            "How empathic did you find the responses you received? What made you feel that way?",
            probes=["Apakah AI terasa berbeda dari manusia?", "Momen spesifik?"],
        ),
        InterviewQuestion(
            "CG3", "Cultural Fit",
            "Apakah komunikasi layanan terasa sesuai dengan harapan budaya Anda sebagai konsumen Indonesia?",
            "Did the service communication feel aligned with your cultural expectations as an Indonesian consumer?",
        ),
        InterviewQuestion(
            "CG4", "Brand Relationship",
            "Bagaimana pengalaman layanan ini mempengaruhi perasaan Anda terhadap mereknya?",
            "How did this service experience affect your feelings towards the brand?",
        ),
        InterviewQuestion(
            "CG5", "Ideal Service",
            "Layanan pelanggan ideal seperti apa yang Anda inginkan dari merek busana Muslim?",
            "What does ideal customer service look like to you from a Muslim fashion brand?",
        ),
    ],
)

AI_SPECIALIST_GUIDE = InterviewGuide(
    target="AI Specialists / Chatbot Developers",
    target_id="Spesialis AI / Pengembang Chatbot",
    objective=(
        "Capture technical and design perspectives on building "
        "empathic AI systems for Indonesian customer service contexts."
    ),
    duration_minutes=60,
    questions=[
        InterviewQuestion(
            "AI1", "Current Capabilities",
            "Sejauh mana chatbot layanan pelanggan saat ini mampu merespons secara empatik?",
            "To what extent are current customer service chatbots capable of empathic responses?",
            probes=["NLP / LLM yang digunakan?", "Batasan teknologi saat ini?"],
        ),
        InterviewQuestion(
            "AI2", "Cultural Localisation",
            "Apa tantangan teknis dalam menyesuaikan AI dengan konteks bahasa dan budaya Indonesia?",
            "What are the technical challenges in adapting AI to Indonesian language and cultural context?",
        ),
        InterviewQuestion(
            "AI3", "Human-AI Handoff",
            "Bagaimana sistem saat ini mengelola eskalasi dari AI ke agen manusia?",
            "How do current systems manage escalation from AI to human agents?",
        ),
        InterviewQuestion(
            "AI4", "Empathy by Design",
            "Menurut Anda, fitur apa yang paling penting untuk membuat AI terasa empatik?",
            "In your view, what features are most important for making AI feel empathic?",
        ),
        InterviewQuestion(
            "AI5", "Future Development",
            "Bagaimana Anda melihat perkembangan AI empatik dalam 3–5 tahun ke depan di konteks Indonesia?",
            "How do you see empathic AI development over the next 3–5 years in the Indonesian context?",
        ),
    ],
)

ALL_GUIDES = {
    "service_agent": SERVICE_AGENT_GUIDE,
    "customer": CUSTOMER_GUIDE,
    "ai_specialist": AI_SPECIALIST_GUIDE,
}
