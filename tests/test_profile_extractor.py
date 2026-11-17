from src.preprocessing.profile_extractor import (
    extract_education,
    extract_experience
)


def test_extract_education():
    text = "B.Tech in Computer Science and MBA"

    result = extract_education(text)

    assert "b.tech" in result
    assert "mba" in result


def test_extract_no_education():
    text = "I enjoy coding and learning new technologies"

    result = extract_education(text)

    assert result == []


def test_extract_experience_keywords():
    text = "Completed an internship and worked as a freelancer"

    result = extract_experience(text)

    assert "internship" in result["experience_mentions"]
    assert "freelancer" in result["experience_mentions"]
    assert "intern" not in result["experience_mentions"]


def test_extract_experience_years():
    text = "Worked for 2 years and 6 months"

    result = extract_experience(text)

    assert "2" in result["years_of_experience"]


def test_extract_empty_text():
    result = extract_experience("")

    assert result == {
        "experience_mentions": [],
        "years_of_experience": []
    }