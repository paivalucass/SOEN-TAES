def minPath(grid, k):
    n = len(grid)
    m = len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    result = float('inf')

    def dfs(path, x, y):
        nonlocal result
        if len(path) == k:
            result = min(result, path)
            return
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                path.append(grid[nx][ny])
                dfs(path, nx, ny)
                path.pop()
    for i in range(n):
        for j in range(m):
            dfs([grid[i][j]], i, j)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(minPath([[1,2,3], [4,5,6], [7,8,9]], 3), [1, 2, 1])
        self.assertEqual(minPath([[5,9,3], [4,1,6], [7,8,2]], 1), [1])

if __name__ == '__main__':
    unittest.main()