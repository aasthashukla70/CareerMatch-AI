from src.preprocessing.resume_parser import extract_text_from_pdf
from src.preprocessing.text_cleaner import clean_text
from src.preprocessing.skill_extractor import extract_skills
from src.preprocessing.profile_extractor import (
    extract_education,
    extract_experience
)


def process_resume(file_path: str) -> dict:
    """
    Extract, clean, and analyze resume information.
    """

    raw_text = extract_text_from_pdf(file_path)

    cleaned_text = clean_text(raw_text)

    skills = extract_skills(cleaned_text)

    education = extract_education(cleaned_text)

    experience = extract_experience(cleaned_text)

    return {
        "raw_text": raw_text,
        "cleaned_text": cleaned_text,
        "character_count": len(cleaned_text),
        "skills": skills,
        "education": education,
        "experience": experience
    }