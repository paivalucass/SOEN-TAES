def minimum(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a if a < b else b
    else:
        return "Invalid Input"
import unittest

class Test(unittest.TestCase):
    def test_minimum(self):
        self.assertEqual(minimum(1, 2), 1)

if __name__ == '__main__':
    unittest.main()