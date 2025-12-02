def count_no_of_ways(n, k):
    if n == 0:
        return 0
    same, diff = 0, k
    for i in range(2, n+1):
        same, diff = diff, (same + diff) * (k-1)
    return same + diff

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_no_of_ways(2, 4), 16)

if __name__ == '__main__':
    unittest.main()