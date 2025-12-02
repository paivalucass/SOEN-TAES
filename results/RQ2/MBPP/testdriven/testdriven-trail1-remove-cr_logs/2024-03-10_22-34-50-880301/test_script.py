import math

def harmonic_sum(n):
    if not isinstance(n, int) or n <= 0:
        return "Invalid Input"
    
    result = 0
    for i in range(1, n+1):
        result += 1 / i
    
    return round(result, 15) if result != float('inf') else "Infinity"
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(harmonic_sum(7), 2.5928571428571425, places=15)

if __name__ == '__main__':
    unittest.main()