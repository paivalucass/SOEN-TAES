def centered_hexagonal_number(n):
    if n <= 0:
        return 0
    else:
        return 3*n*(n-1) + 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(centered_hexagonal_number(10), 271)

if __name__ == '__main__':
    unittest.main()