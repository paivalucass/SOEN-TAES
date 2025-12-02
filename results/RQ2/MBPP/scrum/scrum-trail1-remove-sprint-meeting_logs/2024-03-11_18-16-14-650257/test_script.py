def centered_hexagonal_number(n: int) -> int:
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    result = 3 * n * (n - 1) + 1
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(centered_hexagonal_number(10), 271)

if __name__ == '__main__':
    unittest.main()