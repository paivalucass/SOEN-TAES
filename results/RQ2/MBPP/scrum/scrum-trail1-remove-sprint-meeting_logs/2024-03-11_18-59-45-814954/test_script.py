def largest_subset(a):
    count = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] % a[j] == 0 or a[j] % a[i] == 0:
                count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test_largest_subset(self):
        self.assertEqual(largest_subset([ 1, 3, 6, 13, 17, 18 ]), 4)

if __name__ == '__main__':
    unittest.main()