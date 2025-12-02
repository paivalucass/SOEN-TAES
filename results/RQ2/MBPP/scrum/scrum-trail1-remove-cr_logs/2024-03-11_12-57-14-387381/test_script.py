import math

def harmonic_sum(n):
  if n <= 1:
    return 0
  else:
    total = 0.0
    for i in range(1, n+1):
      total += 1/i
    return total
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(harmonic_sum(7), 2.5928571428571425, delta=0.001)

if __name__ == '__main__':
    unittest.main()