def largest_subset(a):
    max_subset = 0
    n = len(a)
    for i in range(n):
        for j in range(i+1, n):
            count = 0
            for k in range(i, j+1):
                if a[k] % a[i] == 0 or a[i] % a[k] == 0:
                    count += 1
            if count == j - i + 1:
                subset_size = j - i + 1
                if subset_size > max_subset:
                    max_subset = subset_size
    return max_subset
import unittest

class Test(unittest.TestCase):
    def test_largest_subset(self):
        self.assertEqual(largest_subset([ 1, 3, 6, 13, 17, 18 ]), 4)

if __name__ == '__main__':
    unittest.main()