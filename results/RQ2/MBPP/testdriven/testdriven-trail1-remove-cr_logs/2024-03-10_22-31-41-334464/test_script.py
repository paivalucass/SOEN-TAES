def multiply_int(x, y):
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError("Inputs x and y must be integers")
        
    return x * y

import unittest

class Test(unittest.TestCase):
    def test_multiply_int(self):
        self.assertEqual(multiply_int(10, 20), 200)

if __name__ == '__main__':
    unittest.main()