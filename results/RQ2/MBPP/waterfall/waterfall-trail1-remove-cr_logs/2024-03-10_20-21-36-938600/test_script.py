def max_product(arr):
    if not arr:
        return 0
    
    n = len(arr)
    max_product = 0
    dp = [1] * n
    
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] * arr[i])
        
        max_product = max(max_product, dp[i])
    
    return max_product
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_product([3, 100, 4, 5, 150, 6]), 3000)

if __name__ == '__main__':
    unittest.main()