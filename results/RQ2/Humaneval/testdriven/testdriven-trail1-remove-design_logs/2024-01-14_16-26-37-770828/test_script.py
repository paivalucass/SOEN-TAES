def minPath(grid, k):
    n = len(grid)
    m = len(grid[0])

    def dfs(x, y, k, path):
        if k == 0:
            return [grid[x][y]]
        res = None
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                path.add((x, y))
                if (nx, ny) not in path:
                    new_path = dfs(nx, ny, k - 1, path)
                    if new_path is not None:
                        if res is None or new_path < res:
                            res = new_path
                path.remove((x, y))
        if res is not None:
            return [grid[x][y]] + res

    for i in range(n):
        for j in range(m):
            path = set()
            result = dfs(i, j, k, path)
            if result is not None:
                return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(minPath([[1,2,3], [4,5,6], [7,8,9]], 3), [1, 2, 1])
        self.assertEqual(minPath([[5,9,3], [4,1,6], [7,8,2]], 1), [1])

if __name__ == '__main__':
    unittest.main()