import spacy
from .cleaner import clean_resume_text  # ✅ Ensure cleaner.py exists and has clean_resume_text

import spacy

nlp = spacy.load("en_core_web_sm")


# ✅ Define common skills for matching
COMMON_SKILLS = {
    "python", "sql", "excel", "tableau", "power bi", "data analysis", "machine learning",
    "teamwork", "communication", "leadership", "financial analysis", "problem solving",
    "marketing", "project management", "graphic design", "html", "css", "javascript", 
    "sales", "negotiation", "customer service", "biotechnology", "chemistry", 
    "legal research", "contract law", "data visualization", "statistics", "teaching",
    "counseling", "ai", "creativity", "networking", "public speaking", "presentation"
}

# ✅ Extract matched skills
def extract_skills(text: str):
    text = text.lower()
    return list({skill for skill in COMMON_SKILLS if skill in text})

# ✅ Extract named entities using spaCy
def extract_entities(text: str):
    doc = nlp(text)
    entities = {}
    for ent in doc.ents:
        label = ent.label_
        value = ent.text.strip()
        if value not in entities.get(label, []):
            entities.setdefault(label, []).append(value)
    return entities

# ✅ Main wrapper function used in app.py
def extract_info(text: str) -> dict:
    cleaned = clean_resume_text(text)
    return {
        "skills": extract_skills(cleaned),
        "entities": extract_entities(cleaned)
    }
