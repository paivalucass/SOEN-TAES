def multiply_int(x, y):
    try:
        result = int(x) * int(y)
        return result
    except ValueError:
        return "Error"
import unittest

class Test(unittest.TestCase):
    def test_multiply_int(self):
        self.assertEqual(multiply_int(10, 20), 200)

if __name__ == '__main__':
    unittest.main()