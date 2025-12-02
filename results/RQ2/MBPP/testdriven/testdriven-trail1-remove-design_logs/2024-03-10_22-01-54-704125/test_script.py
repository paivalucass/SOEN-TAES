import math

def next_Perfect_Square(number):
    if not isinstance(number, int) or number <= 0:
        return 'Input must be a positive integer'
    return math.ceil(number**0.5)**2
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(next_Perfect_Square(35), 36)

if __name__ == '__main__':
    unittest.main()