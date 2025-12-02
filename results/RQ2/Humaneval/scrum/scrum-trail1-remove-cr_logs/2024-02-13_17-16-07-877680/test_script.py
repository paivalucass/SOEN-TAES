def is_equal_to_sum_even(n):
    count = 0
    for i in range(2, n // 2 + 1, 2):
        if n - i in range(2, n + 1, 2):
            count += 1
    return count == 4
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_equal_to_sum_even(4), False)
        self.assertEqual(is_equal_to_sum_even(6), False)
        self.assertEqual(is_equal_to_sum_even(8), True)

if __name__ == '__main__':
    unittest.main()