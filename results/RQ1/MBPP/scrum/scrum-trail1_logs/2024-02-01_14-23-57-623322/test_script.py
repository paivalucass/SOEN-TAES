def centered_hexagonal_number(n):
    if not isinstance(n, int) or n < 0:
        return "Error: Invalid Input"
    elif n == 0:
        return "Some value for n=0"
    else:
        return 3 * n * n - 3 * n + 1

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(centered_hexagonal_number(10), 271)

if __name__ == '__main__':
    unittest.main()