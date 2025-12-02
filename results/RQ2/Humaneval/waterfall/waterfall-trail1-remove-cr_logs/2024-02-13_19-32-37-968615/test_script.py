import math

def max_fill(grid, capacity):
    if not grid or not grid[0]:
        return 'Invalid input grid'
    for row in grid:
        if len(row) != len(grid[0]):
            return 'Invalid input grid'
    if capacity > 10:
        return 'Invalid input capacity'
    dp = [[math.inf] * len(grid[0]) for _ in range(len(grid))]
    dp[0][0] = grid[0][0]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j] + grid[i][j])
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j-1] + grid[i][j])
    return dp[-1][-1]
import unittest

class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1), 6)

    def test_example2(self):
        self.assertEqual(max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2), 5)

    def test_example3(self):
        self.assertEqual(max_fill([[0,0,0], [0,0,0]], 5), 0)

if __name__ == '__main__':
    unittest.main()