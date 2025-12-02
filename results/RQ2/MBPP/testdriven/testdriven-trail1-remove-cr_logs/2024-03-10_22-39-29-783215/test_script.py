def minimum(a, b):
    if a < b:
        return a
    elif b < a:
        return b
    else:
        return "The numbers are equal"
import unittest

class Test(unittest.TestCase):
    def test_minimum(self):
        self.assertEqual(minimum(1, 2), 1)

if __name__ == '__main__':
    unittest.main()