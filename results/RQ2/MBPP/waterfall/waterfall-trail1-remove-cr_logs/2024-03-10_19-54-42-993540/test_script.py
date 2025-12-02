def hexagonal_num(n):
    if n < 1:
        return "Error: Input value of n should be greater than or equal to 1"
    else:
        return 2*n*n - n
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(hexagonal_num(10), 190)

if __name__ == '__main__':
    unittest.main()