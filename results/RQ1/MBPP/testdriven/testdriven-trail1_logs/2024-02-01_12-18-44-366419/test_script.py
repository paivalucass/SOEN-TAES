def babylonian_squareroot(number):
    """
    Compute the square root of the input number using the Babylonian method.

    Args:
    number (int or float): The input number for which the square root needs to be computed.

    Returns:
    float: The square root of the input number.

    Raises:
    ValueError: If the input number is negative.
    """

    if not isinstance(number, (int, float)):
        raise ValueError("Input number must be an int or float")

    if number < 0:
        raise ValueError("Input number cannot be negative")

    approximation = number / 2
    while abs(approximation * approximation - number) > 0.001:
        approximation = (approximation + number / approximation) / 2

    return round(approximation, 3)
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(babylonian_squareroot(10), 3.162277660168379, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()