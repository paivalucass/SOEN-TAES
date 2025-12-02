def count_no_of_ways(n, k):
    if n <= 0 or k <= 0:
        return "Error"
    if n == 1:
        return k
    same, diff = k, k * (k - 1)
    for i in range(3, n + 1):
        same, diff = diff, (same + diff) * (k - 1)
    return same + diff
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_no_of_ways(2, 4), 16)

if __name__ == '__main__':
    unittest.main()