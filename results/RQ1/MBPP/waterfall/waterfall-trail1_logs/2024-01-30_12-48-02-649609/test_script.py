import math

def harmonic_sum(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    result = sum(1/i for i in range(1, n+1))

    return round(result, 15)
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(harmonic_sum(7), 2.5928571428571425)

if __name__ == '__main__':
    unittest.main()