def get_coordinates(coordinate, grid_size):
    x, y = coordinate
    adjacent_coordinates = []
    for i in range(max(0, x-1), min(grid_size[0], x+2)):
        for j in range(max(0, y-1), min(grid_size[1], y+2)):
            if (i, j) != (x, y):
                adjacent_coordinates.append([i, j])
    return adjacent_coordinates

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(adjac((3, 4)), [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]])

if __name__ == '__main__':
    unittest.main()