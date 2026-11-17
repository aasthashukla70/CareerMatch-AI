import re


# Common education qualifications
EDUCATION_KEYWORDS = [
    "b.tech",
    "b.e.",
    "bachelor of technology",
    "bachelor of engineering",
    "b.sc",
    "bachelor of science",
    "bca",
    "bachelor of computer applications",
    "m.tech",
    "master of technology",
    "m.sc",
    "master of science",
    "mca",
    "master of computer applications",
    "mba",
    "phd",
    "diploma",
    "high school",
    "12th",
    "10th"
]


def extract_education(text: str) -> list:
    """
    Extract education qualifications from resume text.
    """

    if not text:
        return []

    text = text.lower()

    extracted_education = []

    for qualification in EDUCATION_KEYWORDS:

        pattern = re.escape(qualification)

        if re.search(pattern, text):
            extracted_education.append(qualification)

    return extracted_education


def extract_experience(text: str) -> dict:
    """
    Identify experience-related information from resume text.
    """

    if not text:
        return {
            "experience_mentions": [],
            "years_of_experience": []
        }

    text = text.lower()

    experience_mentions = []

    keywords = [
        "internship",
        "intern",
        "work experience",
        "professional experience",
        "employment",
        "freelancer"
    ]

    for keyword in keywords:
        pattern = r'\b' + re.escape(keyword) + r'\b'

        if re.search(pattern, text):
            experience_mentions.append(keyword)

    years_pattern = r'\b(\d+(?:\.\d+)?)\s*\+?\s*(?:years?|yrs?)\b'

    years_of_experience = re.findall(years_pattern, text)

    return {
        "experience_mentions": experience_mentions,
        "years_of_experience": years_of_experience
    }