#func
def pos_neg_zero(num):
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"

def n_primes(n) -> list[int]:
    primes = []
    candidate = 2
    while len(primes) < n:
        # check if candidate is prime, trial division up to sqrt(n)
        is_prime = True
        for p in range(2, int(candidate ** 0.5) + 1):
            if candidate % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
        candidate += 1
    return primes

def sum_1_to_n(n):
    return sum(range(1, n + 1))


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
    