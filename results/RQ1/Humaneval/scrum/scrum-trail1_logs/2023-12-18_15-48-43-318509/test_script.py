def minPath(grid, k):
    N = len(grid)
    cells = []
    for i in range(N):
        for j in range(N):
            cells.append((grid[i][j], i, j))
    cells.sort()
    start = cells[0][1:]
    path = [grid[start[0]][start[1]]]
    while len(path) < k:
        x, y = start
        neighbors = [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]
        next_cell = None
        for neighbor in neighbors:
            if neighbor[0] >= 0 and neighbor[0] < N and neighbor[1] >= 0 and neighbor[1] < N:
                if next_cell is None or grid[neighbor[0]][neighbor[1]] < grid[next_cell[0]][next_cell[1]]:
                    next_cell = neighbor
        path.append(grid[next_cell[0]][next_cell[1]])
        start = next_cell
    return path
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(minPath([[1,2,3], [4,5,6], [7,8,9]], 3), [1, 2, 1])
        self.assertEqual(minPath([[5,9,3], [4,1,6], [7,8,2]], 1), [1])

if __name__ == '__main__':
    unittest.main()