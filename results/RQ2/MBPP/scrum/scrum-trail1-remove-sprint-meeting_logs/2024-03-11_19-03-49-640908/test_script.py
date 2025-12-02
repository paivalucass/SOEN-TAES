def maxAverageOfPath(cost):
    if not cost:
        return 0
    if len(cost) != len(cost[0]):
        return 0
    
    n = len(cost)
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = cost[0][0]
    
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + cost[i][0]  
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + cost[0][j]  
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + cost[i][j]  

    return dp[n-1][n-1] / (2*n-1)

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Valid Input Matrix - Additional Test Data",
      "Input Data": "cost=[[1, 2, 3], [6, 5, 4], [7, 3, 9], [2, 4, 6]]",
      "Expected Output": "5.2"
    },
    {
      "Test Title": "Valid Input Matrix - All Negative Values",
      "Input Data": "cost=[[-1, -2, -3], [-6, -5, -4], [-7, -3, -9]]",
      "Expected Output": "-3.83"
    },
    {
      "Test Title": "Empty Input Matrix",
      "Input Data": "cost=[]",
      "Expected Output": "Error: Invalid input matrix"
    },
    {
      "Test Title": "Non-Square Input Matrix",
      "Input Data": "cost=[[1, 2, 3], [6, 5, 4], [7, 3, 9], [4, 5, 6]]",
      "Expected Output": "Error: Input matrix is not a square matrix"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]), 5.2)

if __name__ == '__main__':
    unittest.main()