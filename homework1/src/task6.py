import string

def num_words(filename: str) -> int:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    # Remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    content = content.translate(translator)
    # Split by any whitespace and count
    words = content.split()
    return len(words)