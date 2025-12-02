def multiply_int(x, y):
    if not isinstance(x, int) or not isinstance(y, int):
        return "Invalid input data"
    
    product = x * y
    return product
import unittest

class Test(unittest.TestCase):
    def test_multiply_int(self):
        self.assertEqual(multiply_int(10, 20), 200)

if __name__ == '__main__':
    unittest.main()