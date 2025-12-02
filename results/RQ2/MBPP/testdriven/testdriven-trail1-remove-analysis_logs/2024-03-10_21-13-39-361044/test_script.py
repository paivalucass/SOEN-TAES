def babylonian_squareroot(number, tolerance=0.0001):
    '''
    Write a function for computing square roots using the babylonian method.
    assert math.isclose(babylonian_squareroot(10), 3.162277660168379, rel_tol=0.001)
    '''
    import math
    if number < 0:
        raise ValueError("Input must be a positive number")
    if number == 0:
        return 0
    guess = number / 2
    while abs(guess * guess - number) > tolerance:
        guess = (guess + number / guess) / 2
    return guess
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(babylonian_squareroot(10), 3.162277660168379, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()