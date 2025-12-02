def babylonian_squareroot(number):
    if not isinstance(number, (int, float)):
        return "Error: Invalid input"
    if number < 0:
        return "Error: Invalid input"
    if number == 0:
        return 0
    guess = number / 2.0
    while True:
        new_guess = (guess + number / guess) / 2
        if abs(new_guess - guess) < 0.0001:
            return round(new_guess, 11)
        guess = new_guess
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(babylonian_squareroot(10), 3.162277660168379, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()
