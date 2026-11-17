import re


def clean_text(text: str) -> str:
    """
    Clean and normalize extracted resume text.
    """

    if not text:
        return ""

    # Convert text to lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r'https?://\S+|www\.\S+', ' ', text)

    # Remove email addresses
    text = re.sub(
        r'\b[\w.-]+@[\w.-]+\.\w+\b',
        ' ',
        text
    )

    # Remove phone numbers
    text = re.sub(
        r'\+?\d[\d\s()-]{8,}\d',
        ' ',
        text
    )

    # Remove unwanted special characters
    # Preserve +, # and . for technical terms
    text = re.sub(r'[^a-z0-9+#.%\s]', ' ', text)

    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)

    return text.strip()