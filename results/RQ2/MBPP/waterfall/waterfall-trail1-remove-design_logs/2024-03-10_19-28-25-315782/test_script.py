def centered_hexagonal_number(n):
    if not isinstance(n, int) or n < 1:
        return "Error: Invalid input"
    elif n > 1000000:
        return "Error: Input exceeds system limitations"
    else:
        return n * (2 * n + 1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(centered_hexagonal_number(10), 271)

if __name__ == '__main__':
    unittest.main()