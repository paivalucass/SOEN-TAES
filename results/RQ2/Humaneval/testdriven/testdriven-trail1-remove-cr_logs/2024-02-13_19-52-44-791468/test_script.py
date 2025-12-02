def is_equal_to_sum_even(n):
    if n % 2 != 0 or n < 0:
        return False
    if n == 0:
        return True
    return n % 8 == 0
import unittest

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(is_equal_to_sum_even(4), False)

    def test_2(self):
        self.assertEqual(is_equal_to_sum_even(6), False)

    def test_3(self):
        self.assertEqual(is_equal_to_sum_even(8), True)

if __name__ == '__main__':
    unittest.main()