def centered_hexagonal_number(n):
    if n == 1:
        return 1
    else:
        return 3*n*n - 3*n + 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(centered_hexagonal_number(10), 271)

if __name__ == '__main__':
    unittest.main()