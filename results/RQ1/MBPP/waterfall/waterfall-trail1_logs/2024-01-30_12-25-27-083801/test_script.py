def centered_hexagonal_number(n):
    result = 3 * n**2 - 3 * n + 1
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(centered_hexagonal_number(10), 271)

if __name__ == '__main__':
    unittest.main()