def max_sum_increasing_subseq(a, n, index, k):
    '''Write a function to find the maximum sum of increasing subsequence from prefix until ith index and also including a given kth element which is after i, i.e., k > i.'''
    max_sum = 0
    dp = [0] * n  # Initialize an array for dynamic programming
    
    # Calculate the maximum sum of increasing subsequence
    for i in range(n):
        dp[i] = a[i]
        for j in range(i):
            if a[i] > a[j]:
                dp[i] = max(dp[i], dp[j] + a[i])
    
    # Calculate the maximum sum including the kth element
    for i in range(n):
        if i < index and a[i] < a[index]:
            max_sum = max(max_sum, dp[i])
    max_sum += a[index]
    for i in range(index+1, n):
        if a[i] > a[index]:
            max_sum = max(max_sum, dp[i] + a[index])
    
    # Return the maximum sum
    return max_sum + a[k] if k > index else max_sum

# Test the function with the given input to ensure it returns 11
assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5], 7, 4, 6) == 11
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5], 7, 4, 6), 11)

if __name__ == '__main__':
    unittest.main()