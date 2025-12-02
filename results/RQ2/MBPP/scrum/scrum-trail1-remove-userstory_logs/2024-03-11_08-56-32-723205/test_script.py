def hexagonal_num(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")

    result = 2*n**2 - n
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(hexagonal_num(10), 190)

if __name__ == '__main__':
    unittest.main()