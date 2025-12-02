def minPath(grid, k):
    if k % 2 == 0:
        return [min(range(1, len(grid)*len(grid[0]) + 1)]

    n = len(grid)
    m = len(grid[0])
    return [grid[0][0], grid[n-1][0], grid[0][m-1]]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(minPath([[1,2,3], [4,5,6], [7,8,9]], 3), [1, 2, 1])
        self.assertEqual(minPath([[5,9,3], [4,1,6], [7,8,2]], 1), [1])

if __name__ == '__main__':
    unittest.main()