def pos_neg_zero(num):
    """
    Determine if a number is positive, negative, or zero.

    Args:
        num (int or float): The number to evaluate.

    Returns:
        str: "positive" if num > 0,
             "negative" if num < 0,
             "zero" if num == 0.
    """
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"


def n_primes(n) -> list[int]:
    """
    Generate the first n prime numbers.

    Args:
        n (int): The number of prime numbers to generate.

    Returns:
        list[int]: A list containing the first n prime numbers.
    """
    primes = []
    candidate = 2
    while len(primes) < n:
        # Check if candidate is prime using trial division up to sqrt(candidate)
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
    """
    Calculate the sum of all integers from 1 to n (inclusive).

    Args:
        n (int): The upper bound of the range.

    Returns:
        int: The sum of all integers from 1 to n.
    """
    return sum(range(1, n + 1))