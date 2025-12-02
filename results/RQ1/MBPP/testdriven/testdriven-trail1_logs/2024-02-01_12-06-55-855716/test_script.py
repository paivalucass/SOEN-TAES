def multiply_int(x, y):
    try:
        if isinstance(x, int) and isinstance(y, int):
            result = x * y
            return result
        else:
            return "Error: Both x and y must be valid integers"
    except Exception as e:
        return "Error: An unexpected error occurred"
import unittest

class Test(unittest.TestCase):
    def test_multiply_int(self):
        self.assertEqual(multiply_int(10, 20), 200)

if __name__ == '__main__':
    unittest.main()