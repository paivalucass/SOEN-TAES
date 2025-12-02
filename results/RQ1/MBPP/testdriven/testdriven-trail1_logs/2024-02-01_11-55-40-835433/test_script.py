def is_divisible_by_11(n):
    return n % 11 == 0

assert is_divisible_by_11(12345) == False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Diff(12345), False)

if __name__ == '__main__':
    unittest.main()