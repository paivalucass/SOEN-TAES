def babylonian_squareroot(number):
    if number < 0:
        raise ValueError("Input must be a non-negative number")
    
    guess = number / 2
    while abs(guess*guess - number) > 0.0001:
        guess = (guess + number/guess) / 2
    return guess
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(babylonian_squareroot(10), 3.162277660168379, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()