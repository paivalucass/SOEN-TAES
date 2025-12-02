def find_Parity(x):
    if not isinstance(x, int) or x < 0:
        raise ValueError("Input must be a non-negative integer.")

    return x % 2 != 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Parity(12), False)

if __name__ == '__main__':
    unittest.main()