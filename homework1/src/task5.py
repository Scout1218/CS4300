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

def first_n(list_to_return: list, n: int) -> list:
    """
    Return the first n elements from a given list.

    Args:
        list_to_return (list): The list to slice.
        n (int): The number of elements to return from the start.

    Returns:
        list: A list containing the first n elements.
    """
    return list_to_return[:n]

