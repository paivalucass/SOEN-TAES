import math

def max_fill(grid, capacity):
    total_water = 0
    for row in grid:
        total_water += sum(row)
    return math.ceil(total_water / capacity)
import unittest

class Test(unittest.TestCase):
    def test_example1(self):
        grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
        self.assertEqual(max_fill(grid, 1), 6)

    def test_example2(self):
        grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
        self.assertEqual(max_fill(grid, 2), 5)

    def test_example3(self):
        grid = [[0,0,0], [0,0,0]]
        self.assertEqual(max_fill(grid, 5), 0)

if __name__ == '__main__':
    unittest.main()