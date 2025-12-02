def minPath(grid, k):
    n = len(grid)
    dp = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dp[i][j] = grid[i][j]

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    path = []

    def dfs(x, y, length, cur_path):
        if length == k:
            path.append(cur_path)
            return
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                dfs(nx, ny, length + 1, cur_path + [grid[nx][ny]])

    for i in range(n):
        for j in range(n):
            dfs(i, j, 1, [dp[i][j]])

    return min(path)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(minPath([[1,2,3], [4,5,6], [7,8,9]], 3), [1, 2, 1])
        self.assertEqual(minPath([[5,9,3], [4,1,6], [7,8,2]], 1), [1])

if __name__ == '__main__':
    unittest.main()