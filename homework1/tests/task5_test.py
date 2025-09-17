import re
import task5

def test_first_three_books_slicing():
    # test if first 3 of list is equal to slicing first 3
    assert task5.favorite_books[:3] == task5.favorite_books[0:3]

def test_student_database_is_dict():
    # test if student database is a dict
    assert isinstance(task5.students, dict)

def test_student_names_follow_regex():
    # test if student name follows a regex (e.g., only letters)
    name_pattern = re.compile(r'^[A-Za-z]+$')
    for name in task5.students.keys():
        assert name_pattern.match(name), f"Invalid name format: {name}"

def test_student_ids_follow_regex():
    # test if student ID follows a regex (e.g., only digits)
    id_pattern = re.compile(r'^\d+$')
    for student_id in task5.students.values():
        assert id_pattern.match(str(student_id)), f"Invalid ID format: {student_id}"
