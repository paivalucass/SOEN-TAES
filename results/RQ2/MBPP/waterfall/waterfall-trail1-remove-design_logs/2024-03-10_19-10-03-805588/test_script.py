import math

def harmonic_sum(n):
    if n <= 1:
        return "Error"
    else:
        total = 0
        for i in range(1, n+1):
            total += 1/i
        return round(total, 15)
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(harmonic_sum(7), 2.5928571428571425)

if __name__ == '__main__':
    unittest.main()