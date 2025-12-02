def count_no_of_ways(n, k):
    if n == 0:
        return 0
    if n == 1:
        return k
    same = k
    diff = k * (k - 1)
    for i in range(3, n + 1):
        total = (same + diff) * (k - 1)
        same = diff
        diff = total
    return same + diff

import unittest

class Test(unittest.TestCase):
    def test_count_no_of_ways(self):
        self.assertEqual(count_no_of_ways(2, 4), 16)

if __name__ == '__main__':
    unittest.main()