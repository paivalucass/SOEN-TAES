def largest_subset(a):
    if not isinstance(a, list):
        return "Invalid input: input should be a list of numbers"
    
    for num in a:
        if not isinstance(num, int):
            return "Invalid input: list should only contain numbers"
    
    dp = [1] * len(a)
    for i in range(len(a)):
        for j in range(i):
            if a[i] % a[j] == 0 and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    
    return max(dp) if dp else 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(largest_subset([ 1, 3, 6, 13, 17, 18 ]), 4)

if __name__ == '__main__':
    unittest.main()