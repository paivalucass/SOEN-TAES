def find_star_num(n):
    if not isinstance(n, int) or n < 1:
        return "Error"
    if n == 1:
        return 3
    power_of_2 = 2 ** (n - 1)
    star_number = power_of_2 * (2 ** n - 1) - 1
    if star_number > 1000000:
        return "Very Large Number"
    return star_number
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_star_num(3), 37)

if __name__ == '__main__':
    unittest.main()