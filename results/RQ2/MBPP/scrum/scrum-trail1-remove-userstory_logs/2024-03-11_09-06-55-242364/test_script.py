def count_binary_seq(n):
    if n < 0:
        return 0
    else:
        return 2**n
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()