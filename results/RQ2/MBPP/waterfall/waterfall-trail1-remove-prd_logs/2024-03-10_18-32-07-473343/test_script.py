def babylonian_squareroot(number):
    '''Function for computing square roots using the babylonian method.'''
    import math

    if not isinstance(number, (int, float)):
        return "Error: Invalid input type"

    if number < 0:
        return "Error: Negative input number"

    guess = number / 2
    while abs(guess * guess - number) > 0.0001:
        guess = (guess + number / guess) / 2

    return round(guess, 15) if isinstance(number, float) else round(guess, 5)
import unittest
import math

class Test(unittest.TestCase):
    def test_babylonian_squareroot(self):
        self.assertTrue(math.isclose(babylonian_squareroot(10), 3.162277660168379, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()