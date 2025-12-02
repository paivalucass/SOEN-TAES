def minPath(grid, k):
    n = len(grid)

    def dfs(i, j, path):
        if len(path) == k:
            return path
        neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        neighbors = [(x, y) for x, y in neighbors if 0 <= x < n and 0 <= y < n]
        neighbors.sort(key=lambda x: (grid[x[0]][x[1]], (x[0], x[1])))
        for x, y in neighbors:
            if (x, y) not in path:
                ans = dfs(x, y, path + [(x, y)])
                if ans:
                    return ans
        return None

    for i in range(n):
        for j in range(n):
            ans = dfs(i, j, [(i, j)])
            if ans:
                return [grid[x][y] for x, y in ans]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(minPath([[1,2,3], [4,5,6], [7,8,9]], 3), [1, 2, 1])
        self.assertEqual(minPath([[5,9,3], [4,1,6], [7,8,2]], 1), [1])

if __name__ == '__main__':
    unittest.main()