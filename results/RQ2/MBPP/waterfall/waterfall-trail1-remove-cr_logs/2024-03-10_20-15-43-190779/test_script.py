def geometric_sum(n):
    if not isinstance(n, int) or n <= 0:
        return "Invalid input"

    def calculate_geometric_sum(k):
        if k == 0:
            return 1
        else:
            return 1 / (2 ** k) + calculate_geometric_sum(k - 1)

    return round(calculate_geometric_sum(n), 7)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(geometric_sum(7), 1.9921875)

if __name__ == '__main__':
    unittest.main()