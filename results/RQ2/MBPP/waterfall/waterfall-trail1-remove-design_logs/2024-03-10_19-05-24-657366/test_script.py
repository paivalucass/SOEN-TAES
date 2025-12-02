def centered_hexagonal_number(n):
    return n * (3*n - 1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(centered_hexagonal_number(10), 271)

if __name__ == '__main__':
    unittest.main()