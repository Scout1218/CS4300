#tests
#task2
def add_integers(a: int, b :int) -> int:
    return (a + b)

#floats
def divide_integers(a: int, b: int) -> float:
    return (a / b)

#string
def uppercase(string: str) -> str:
    return string.upper()

#bool
def is_even(n: int) -> bool:
    return ((n % 2) == 0)

#test
#example vars
x,y = 5,2
string = "hello"

def test_datatype():
    assert isinstance(add_integers(x,y), int)
    assert isinstance(divide_integers(x,y), float)
    assert isinstance(uppercase(string), str)
    assert isinstance(is_even(x), bool)