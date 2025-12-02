import sys

def multiply_int(x, y):
    result = x * y
    if result > sys.maxsize:
        return 'Result exceeds maximum integer value'
    else:
        return result
import unittest

class Test(unittest.TestCase):
    def test_multiply_int(self):
        self.assertEqual(multiply_int(10, 20), 200)

if __name__ == '__main__':
    unittest.main()