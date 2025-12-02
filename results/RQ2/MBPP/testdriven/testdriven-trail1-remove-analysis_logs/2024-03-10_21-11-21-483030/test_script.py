def hexagonal_num(n):
    # This function calculates the nth hexagonal number using the formula: n * (2 * n - 1)
    return n * (2 * n - 1)

assert hexagonal_num(10) == 190
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(hexagonal_num(10), 190)

if __name__ == '__main__':
    unittest.main()