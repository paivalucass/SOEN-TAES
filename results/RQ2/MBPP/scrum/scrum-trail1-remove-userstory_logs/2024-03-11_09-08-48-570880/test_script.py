def minimum(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Input parameters should be numbers")
    
    if a < b:
        return a
    elif b < a:
        return b
    else:
        return a  # or return b
import unittest

class Test(unittest.TestCase):
    def test_minimum(self):
        self.assertEqual(minimum(1, 2), 1)

if __name__ == '__main__':
    unittest.main()