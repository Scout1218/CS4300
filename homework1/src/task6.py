import string

def num_words(filename: str) -> int:
    """
    Count the number of words in a text file, ignoring punctuation.

    Args:
        filename (str): The path to the text file.

    Returns:
        int: The total number of words in the file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    # Remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    content = content.translate(translator)
    # Split by any whitespace and count
    words = content.split()
    return len(words)