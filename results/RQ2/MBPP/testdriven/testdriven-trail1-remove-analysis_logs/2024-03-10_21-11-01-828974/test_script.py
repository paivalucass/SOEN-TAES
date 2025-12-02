def multiply_int(x, y):
    try:
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError("Error: Invalid input. x and y must be integers.")
        
        result = x * y
        return result
    except TypeError as e:
        return str(e)
import unittest

class Test(unittest.TestCase):
    def test_multiply_int(self):
        self.assertEqual(multiply_int(10, 20), 200)

if __name__ == '__main__':
    unittest.main()