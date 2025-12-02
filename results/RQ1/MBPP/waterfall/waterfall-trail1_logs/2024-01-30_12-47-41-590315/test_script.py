import math

def babylonian_squareroot(number):
    if not isinstance(number, (int, float)):
        return "Error: Invalid input data type"
    if number < 0:
        return "Error: Negative number input"
    if number == 0:
        return 0
    if number > 1000000:
        return "Error: Input value too large"

    approximation = number
    new_approximation = 0
    threshold = 0.0001

    while not math.isclose(approximation, new_approximation, rel_tol=threshold):
        new_approximation = (approximation + number / approximation) / 2
        approximation = new_approximation

    return new_approximation
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(babylonian_squareroot(10), 3.16227766016838)

if __name__ == '__main__':
    unittest.main()