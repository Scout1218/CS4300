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


#########################TESTS###############################
def test_add_ints():
    assert isinstance(add_integers(x,y), int)

def test_divide_ints():
    assert isinstance(divide_integers(x,y), float)

def test_string():
    assert isinstance(uppercase(string), str)

def test_is_even():
    assert isinstance(is_even(x), bool)
