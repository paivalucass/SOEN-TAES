def centered_hexagonal_number(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    if n <= 0:
        raise ValueError("Input must be a positive integer")

    return 3 * n ** 2 - 3 * n + 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(centered_hexagonal_number(10), 271)

if __name__ == '__main__':
    unittest.main()