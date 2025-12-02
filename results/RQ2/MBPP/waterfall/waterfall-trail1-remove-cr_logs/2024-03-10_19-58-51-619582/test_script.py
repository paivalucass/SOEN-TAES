def find_star_num(n):
    if not isinstance(n, int) or n < 1:
        return "Invalid input"
    if n == 1:
        return 7
    star_num = 6 * n * (n - 1) + 1
    if n > 100000:
        return "Efficient performance"
    return star_num
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_star_num(3), 37)

if __name__ == '__main__':
    unittest.main()