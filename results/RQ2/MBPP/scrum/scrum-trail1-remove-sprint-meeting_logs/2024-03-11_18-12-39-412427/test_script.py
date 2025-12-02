import math

def is_woodall(x):
    result = x * math.log2(x)
    return result.is_integer() and (result & (result - 1) == 0)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_woodall(383), True)

if __name__ == '__main__':
    unittest.main()