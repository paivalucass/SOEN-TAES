def minPath(grid, k):
    N = len(grid)
    def dfs(x, y, path):
        if len(path) == k:
            return path
        candidates = [(x + dx, y + dy) for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)] if 0 <= x + dx < N and 0 <= y + dy < N and (x + dx, y + dy) not in path]
        candidates.sort(key=lambda pos: (grid[pos[0]][pos[1]], pos[0], pos[1]))
        for nx, ny in candidates:
            res = dfs(nx, ny, path + [(nx, ny)])
            if res:
                return res
    for i in range(N):
        for j in range(N):
            res = dfs(i, j, [(i, j)])
            if res:
                return [grid[x][y] for x, y in res]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(minPath([[1,2,3], [4,5,6], [7,8,9]], 3), [1, 2, 1])
        self.assertEqual(minPath([[5,9,3], [4,1,6], [7,8,2]], 1), [1])

if __name__ == '__main__':
    unittest.main()