def babylonian_squareroot(number):
    if number < 0:
        return "Error"
    x = number
    y = 1
    while x - y > 0.001:
        x = (x + y) / 2
        y = number / x
    return x
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(babylonian_squareroot(10), 3.162277660168379, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()