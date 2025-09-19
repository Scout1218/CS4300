from task2 import *

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
