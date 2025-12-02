def find_star_num(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer")

    # Calculate star number using the given formula
    star_num = 6 * n**2 - 6 * n + 1
    return star_num
import unittest

class Test(unittest.TestCase):

    def test_find_star_num(self):
        self.assertEqual(find_star_num(3), 37)

if __name__ == '__main__':
    unittest.main()