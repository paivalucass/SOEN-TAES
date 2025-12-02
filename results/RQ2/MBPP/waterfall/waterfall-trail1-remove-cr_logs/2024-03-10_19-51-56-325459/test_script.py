def centered_hexagonal_number(n):
    if not isinstance(n, int) or n <= 0:
        return "Error: n should be a positive whole number"

    return 3 * n * (n - 1) + 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(centered_hexagonal_number(10), 271)

if __name__ == '__main__':
    unittest.main()