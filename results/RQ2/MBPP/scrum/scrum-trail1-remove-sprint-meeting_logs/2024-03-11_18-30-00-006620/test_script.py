def babylonian_squareroot(number):
    if not isinstance(number, (int, float)):
        raise TypeError("Input must be a number")
    if number < 0:
        return "Error: Invalid input"

    guess = number / 2
    tolerance = 0.0001
    while abs(guess * guess - number) > tolerance:
        guess = (guess + number / guess) / 2
    return round(guess, 15) if guess != 0 else 0
import unittest
import math

class Test(unittest.TestCase):
    def test_babylonian_squareroot(self):
        self.assertTrue(math.isclose(babylonian_squareroot(10), 3.162277660168379, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()