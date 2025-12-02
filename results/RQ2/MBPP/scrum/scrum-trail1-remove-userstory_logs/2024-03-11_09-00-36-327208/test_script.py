import math

def harmonic_sum(n):
    if not isinstance(n, int) or n <= 0:
        return "Input should be a positive integer"

    sum_of_reciprocals = 0
    for i in range(1, n+1):
        sum_of_reciprocals += 1 / i
    return round(sum_of_reciprocals, 15) if n <= 1000000 else "Result exceeds maximum limit"
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(harmonic_sum(7), 2.5928571428571425, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()