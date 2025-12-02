def count_no_of_ways(n, k):
    if n <= 0:
        return "Error: Invalid number of posts"
    if k <= 0:
        return "Error: Invalid number of colors"
    if n == 1:
        return k
    same_color = k
    diff_color = k * (k-1)
    total_ways = same_color + diff_color
    for i in range(3, n+1):
        same_color, diff_color = diff_color, total_ways * (k-1)
        total_ways = same_color + diff_color
    return total_ways
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_no_of_ways(2, 4), 16)

if __name__ == '__main__':
    unittest.main()