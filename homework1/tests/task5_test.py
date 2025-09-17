import re
#task5
# List of favorite books (title, author)
favorite_books = [
    ("1984", "George Orwell"),
    ("To Kill a Mockingbird", "Harper Lee"),
    ("The Great Gatsby", "F. Scott Fitzgerald"),
    ("Pride and Prejudice", "Jane Austen"),
    ("The Catcher in the Rye", "J.D. Salinger")
]

# Dictionary of student names and their IDs
students = {
    "Alice": 101,
    "Bob": 102,
    "Charlie": 103
}
#ChatGPT made the list and dict

def first_n(list_to_return , n):
    return list_to_return[:n]
''''''


def test_slicing():
    assert first_n(favorite_books,3) == [
        ("1984", "George Orwell"),
        ("To Kill a Mockingbird", "Harper Lee"),
        ("The Great Gatsby", "F. Scott Fitzgerald")]

def test_dict():
    assert isinstance(students,dict)

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
