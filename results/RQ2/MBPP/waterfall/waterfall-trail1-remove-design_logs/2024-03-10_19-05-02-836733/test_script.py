def is_divisible_by_11(number):
    return number % 11 == 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Diff(12345), False)

if __name__ == '__main__':
    unittest.main()