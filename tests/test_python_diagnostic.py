import pytest
from src.python_diagnostic import (
    calculate_student_statistics,
    assign_grade,
    count_words,
    clean_student_data
)

def test_calculate_student_statistics():
    scores = [78, 45, 89, 56, 32]
    stats = calculate_student_statistics(scores)
    assert stats["Total students"] == 5
    assert stats["Highest score"] == 89
    assert stats["Lowest score"] == 32
    assert stats["Passed"] == 3
    assert stats["Failed"] == 2

def test_assign_grade():
    assert assign_grade(90) == 'A'
    assert assign_grade(75) == 'B'
    assert assign_grade(65) == 'C'
    assert assign_grade(55) == 'D'
    assert assign_grade(40) == 'F'

def test_count_words():
    text = "Hello world! Hello Python."
    full_dict, top_three = count_words(text)
    assert full_dict["hello"] == 2
    assert full_dict["world"] == 1
    assert top_three[0][0] == "hello"

def test_clean_student_data():
    records = [
        {"name": "Ali", "score": 78},
        {"name": "Sara", "score": None},
        {"name": "Ahmed", "score": 92}
    ]
    cleaned, avg = clean_student_data(records)
    assert len(cleaned) == 2
    assert avg == 85.0

def test_errors():
    with pytest.raises(ValueError):
        calculate_student_statistics([])
    with pytest.raises(ValueError):
        assign_grade(150)
    with pytest.raises(TypeError):
        count_words(12345)