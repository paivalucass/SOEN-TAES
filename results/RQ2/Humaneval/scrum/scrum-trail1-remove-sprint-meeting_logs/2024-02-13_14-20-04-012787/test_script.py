def minPath(grid, k):
    n = len(grid)
    start = [(i, j) for i in range(n) for j in range(n)]
    start.sort(key=lambda x: grid[x[0]][x[1]])
    x, y = start[0]
    path = [grid[x][y]]
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set([(x, y)])
    for _ in range(k - 1):
        next_path = []
        for x, y in path:
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    next_path.append((nx, ny))
                    visited.add((nx, ny))
        next_path.sort(key=lambda x: grid[x[0]][x[1]])
        path.append(grid[next_path[0][0]][next_path[0][1]])
    return path
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(minPath([[1,2,3], [4,5,6], [7,8,9]], 3), [1, 2, 1])
        self.assertEqual(minPath([[5,9,3], [4,1,6], [7,8,2]], 1), [1])

if __name__ == '__main__':
    unittest.main()