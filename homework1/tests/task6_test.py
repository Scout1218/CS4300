import string
text = "/home/student/CS4300/homework1/task6_read_me.txt"

def num_words(filename: str) -> int:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    # Remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    content = content.translate(translator)
    # Split by any whitespace and count
    words = content.split()
    return len(words)



#########################TESTS###############################
def test():
    assert num_words(text) == 104