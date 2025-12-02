def babylonian_squareroot(number):
    guess = number / 2.0
    while abs(guess * guess - number) > 0.0001:
        guess = (guess + number / guess) / 2.0
    return guess
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(babylonian_squareroot(10), 3.162277660168379, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()