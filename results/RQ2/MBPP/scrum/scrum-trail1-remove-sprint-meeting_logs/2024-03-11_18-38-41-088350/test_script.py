def maximum(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Input parameters must be numbers")

    try:
        return max(a, b)
    except Exception as e:
        raise ValueError("An error occurred while finding the maximum of the two numbers")
import unittest

class Test(unittest.TestCase):
    def test_maximum(self):
        self.assertEqual(maximum(5, 10), 10)

if __name__ == '__main__':
    unittest.main()