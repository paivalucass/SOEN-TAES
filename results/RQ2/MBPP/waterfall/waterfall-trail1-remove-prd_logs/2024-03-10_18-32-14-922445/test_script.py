import math

def harmonic_sum(n):
    if n <= 0:
        return "Error handling: Input integer must be positive"
    sum = 0
    for i in range(1, n+1):
        sum += 1/i
    return round(sum, 15)
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(harmonic_sum(7), 2.5928571428571425, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()