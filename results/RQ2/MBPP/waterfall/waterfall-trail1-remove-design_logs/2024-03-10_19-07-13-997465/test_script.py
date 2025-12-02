def multiply_int(x, y):
    try:
        if not isinstance(x, int) or not isinstance(y, int):
            raise ValueError("Both x and y must be integers")
        result = x * y
        return result
    except ValueError as ve:
        return str(ve)
import unittest

class Test(unittest.TestCase):
    def test_multiply_int(self):
        self.assertEqual(multiply_int(10, 20), 200)

if __name__ == '__main__':
    unittest.main()