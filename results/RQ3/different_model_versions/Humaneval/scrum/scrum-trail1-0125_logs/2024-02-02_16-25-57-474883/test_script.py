def minPath(grid, k):
    n = len(grid)
    start = [(x, y) for x in range(n) for y in range(n)]
    start.sort(key=lambda pos: grid[pos[0]][pos[1]])
    visited = set()
    path = []
    for x, y in start:
        path.append(grid[x][y])
        visited.add((x, y))
        if len(path) == k:
            return path
        neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        for nx, ny in neighbors:
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                start.append((nx, ny))
    return path
import unittest

class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(minPath([[1,2,3], [4,5,6], [7,8,9]], 3), [1, 2, 1])

    def test_example2(self):
        self.assertEqual(minPath([[5,9,3], [4,1,6], [7,8,2]], 1), [1])

if __name__ == '__main__':
    unittest.main()