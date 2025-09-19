# int
def add_integers(a: int, b: int) -> int:
    """
    Add two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of the two integers.
    """
    return a + b


# floats
def divide_integers(a: int, b: int) -> float:
    """
    Divide one integer by another.

    Args:
        a (int): The numerator.
        b (int): The denominator.

    Returns:
        float: The result of the division.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    return a / b


# string
def uppercase(string: str) -> str:
    """
    Convert a string to uppercase.

    Args:
        string (str): The input string.

    Returns:
        str: The uppercase version of the string.
    """
    return string.upper()


# bool
def is_even(n: int) -> bool:
    """
    Check if an integer is even.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is even, False otherwise.
    """
    return (n % 2) == 0


