def minPath(grid, k):
    n = len(grid)
    m = len(grid[0])
    start = min(min(row) for row in grid)
    path = [start]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set([(i, j) for i in range(n) for j in range(m) if grid[i][j] == start])

    while len(path) < k:
        next_val = float('inf')
        next_cell = None
        for i, j in visited:
            for x, y in directions:
                new_i, new_j = i + x, j + y
                if 0 <= new_i < n and 0 <= new_j < m and (new_i, new_j) not in visited:
                    if grid[new_i][new_j] < next_val:
                        next_val = grid[new_i][new_j]
                        next_cell = (new_i, new_j)
        path.append(next_val)
        visited.add(next_cell)

    return path
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(minPath([[1,2,3], [4,5,6], [7,8,9]], 3), [1, 2, 1])
        self.assertEqual(minPath([[5,9,3], [4,1,6], [7,8,2]], 1), [1])

if __name__ == '__main__':
    unittest.main()