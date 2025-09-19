from task3 import *

#########################TESTS###############################
def test_pos_neg_zero_positive():
    assert pos_neg_zero(3) == "positive"

def test_pos_neg_zero_negative():
    assert pos_neg_zero(-3) == "negative"

def test_pos_neg_zero_zero():
    assert pos_neg_zero(0) == "zero"

def test_n_primes():
    assert n_primes(10) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def test_sum_1_to_n():
    assert sum_1_to_n(100) == 5050
    