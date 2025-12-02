def minPath(grid, k):
    n = len(grid)
    m = len(grid[0])
    visited = [[False]*m for _ in range(n)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    directions = ['R', 'D', 'L', 'U']
    def isValid(x, y):
        return 0 <= x < n and 0 <= y < m
    def dfs(x, y, path):
        if len(path) == k:
            return path
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if isValid(nx, ny) and not visited[nx][ny]:
                visited[nx][ny] = True
                res = dfs(nx, ny, path + [grid[nx][ny]])
                if res:
                    return res
                visited[nx][ny] = False
        return None
    for i in range(n):
        for j in range(m):
            visited = [[False]*m for _ in range(n)]
            visited[i][j] = True
            res = dfs(i, j, [grid[i][j]])
            if res:
                return res
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(minPath([[1,2,3], [4,5,6], [7,8,9]], 3), [1, 2, 1])
        self.assertEqual(minPath([[5,9,3], [4,1,6], [7,8,2]], 1), [1])

if __name__ == '__main__':
    unittest.main()