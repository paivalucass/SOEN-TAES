def minPath(grid, k):
    n = len(grid)
    m = len(grid[0])
    visited = [[False]*m for _ in range(n)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    ans = float('inf')
    def dfs(i, j, path):
        if len(path) == k:
            nonlocal ans
            ans = min(ans, path)
            return
        for dx, dy in directions:
            x, y = i + dx, j + dy
            if 0 <= x < n and 0 <= y < m and not visited[x][y]:
                visited[x][y] = True
                dfs(x, y, path + [grid[x][y]])
                visited[x][y] = False
    for i in range(n):
        for j in range(m):
            visited[i][j] = True
            dfs(i, j, [grid[i][j]])
            visited[i][j] = False
    return ans
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(minPath([[1,2,3], [4,5,6], [7,8,9]], 3), [1, 2, 1])
        self.assertEqual(minPath([[5,9,3], [4,1,6], [7,8,2]], 1), [1])

if __name__ == '__main__':
    unittest.main()