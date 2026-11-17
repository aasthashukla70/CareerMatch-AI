from src.preprocessing.skill_extractor import extract_skills


def test_extract_multiple_skills():
    text = "Python, Java, SQL and Machine Learning"

    result = extract_skills(text)

    assert "python" in result
    assert "java" in result
    assert "sql" in result
    assert "machine learning" in result


def test_extract_no_skills():
    text = "I enjoy reading books and playing football"

    result = extract_skills(text)

    assert result == []


def test_extract_empty_text():
    result = extract_skills("")

    assert result == []


def test_case_insensitive():
    text = "PYTHON and MACHINE LEARNING"

    result = extract_skills(text)

    assert "python" in result
    assert "machine learning" in result