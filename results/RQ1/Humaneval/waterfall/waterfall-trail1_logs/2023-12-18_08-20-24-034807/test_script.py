def starts_one_ends(n):
    count_start_with_1 = 9 * (10 ** (n-1))
    count_end_with_1 = 10 ** (n-1)
    total_count = count_start_with_1 + count_end_with_1 - (9 * (10 ** (n-2)))
    return total_count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(starts_one_ends(1), 1)
        self.assertEqual(starts_one_ends(2), 19)
        self.assertEqual(starts_one_ends(3), 271)

if __name__ == '__main__':
    unittest.main()