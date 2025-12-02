def largest_subset(a):
    if not isinstance(a, list):
        return "Invalid Input"
    if not all(isinstance(x, int) for x in a):
        return "Invalid Input"
    if len(a) <= 1:
        return len(a)

    dp = [1] * len(a)
    for i in range(1, len(a)):
        for j in range(i):
            if a[i] % a[j] == 0:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)
import unittest

class Test(unittest.TestCase):
    def test_largest_subset(self):
        self.assertEqual(largest_subset([ 1, 3, 6, 13, 17, 18 ]), 4)

if __name__ == '__main__':
    unittest.main()