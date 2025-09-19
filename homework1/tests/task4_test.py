
from task4 import calculate_discount

#########################TESTS###############################
#ChatGPT test cases:
def test_integer_inputs():
    assert calculate_discount(100, 20) == 80
    assert calculate_discount(50, 50) == 25

def test_float_inputs():
    assert calculate_discount(100.0, 20.0) == 80.0
    assert calculate_discount(59.99, 10.0) == 53.991

def test_mixed_types():
    assert calculate_discount(100, 12.5) == 87.5
    assert calculate_discount(199.99, 25) == 149.9925

def test_zero_discount():
    assert calculate_discount(100, 0) == 100

def test_full_discount():
    assert calculate_discount(100, 100) == 0
