def get_adjacent_coordinates(coord, grid_width, grid_height):
    if not isinstance(coord, tuple) or len(coord) != 2 or not all(isinstance(x, (int, float)) for x in coord):
        raise ValueError("Invalid input coordinates. Please provide a valid coordinate tuple.")
    x, y = coord
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    adjacent_coords = []
    for dx, dy in directions:
        adj_x, adj_y = x + dx, y + dy
        if 0 <= adj_x < grid_width and 0 <= adj_y < grid_height:
            adjacent_coords.append([adj_x, adj_y])
    return adjacent_coords
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(adjac((3, 4)), [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]])

if __name__ == '__main__':
    unittest.main()