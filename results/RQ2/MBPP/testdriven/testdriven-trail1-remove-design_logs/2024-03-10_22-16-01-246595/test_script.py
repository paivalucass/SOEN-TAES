def maxAverageOfPath(cost):
    '''Given a square matrix of size N*N given as a list of lists, where each cell is associated with a specific cost. A path is defined as a specific sequence of cells that starts from the top-left cell move only right or down and ends on bottom right cell. We want to find a path with the maximum average over all existing paths. Average is computed as total cost divided by the number of cells visited in the path.'''
    n = len(cost)
    m = len(cost[0])
    dp = [[0.0] * (m + 1) for _ in range(n + 1)]  # creating a 2D array for dynamic programming

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = cost[i - 1][j - 1] + max(dp[i - 1][j], dp[i][j - 1])  # calculating the maximum cost path

    return dp[n][m] / (n + m - 1)  # returning the maximum average cost of the path
assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]), 5.2)

if __name__ == '__main__':
    unittest.main()