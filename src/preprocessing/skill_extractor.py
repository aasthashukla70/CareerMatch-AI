import re


# Initial technical skills database
SKILLS_DATABASE = [
    "python",
    "java",
    "c++",
    "c#",
    "sql",
    "machine learning",
    "deep learning",
    "natural language processing",
    "data science",
    "data analysis",
    "artificial intelligence",
    "scikit-learn",
    "pandas",
    "numpy",
    "matplotlib",
    "tensorflow",
    "pytorch",
    "opencv",
    "nlp",
    "html",
    "css",
    "javascript",
    "react",
    "node.js",
    "flask",
    "fastapi",
    "django",
    "mongodb",
    "mysql",
    "postgresql",
    "git",
    "github",
    "docker",
    "linux",
    "aws",
    "azure",
    "statistics",
    "excel",
    "power bi",
    "tableau"
]


def extract_skills(text: str) -> list:
    """
    Identify technical skills mentioned in resume text.
    """

    if not text:
        return []

    text = text.lower()

    extracted_skills = []

    for skill in SKILLS_DATABASE:

        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

        if re.search(pattern, text):
            extracted_skills.append(skill)

    return extracted_skills