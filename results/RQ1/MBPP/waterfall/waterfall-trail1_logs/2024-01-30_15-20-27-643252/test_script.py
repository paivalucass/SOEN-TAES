import math

def harmonic_sum(n):
    if n <= 0:
        return "Invalid input. n must be a positive integer."
    else:
        result = 0
        for i in range(1, n+1):
            result += 1/i
        return round(result, 15)
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(harmonic_sum(7), 2.5928571428571425)

if __name__ == '__main__':
    unittest.main()