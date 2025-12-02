import math

def max_fill(grid, capacity):
    if not isinstance(grid, list) or not all(isinstance(row, list) for row in grid):
        raise ValueError("Invalid grid input")
    if not all(all(val == 0 or val == 1 for val in row) for row in grid):
        raise ValueError("Invalid grid values")
    if not isinstance(capacity, int) or capacity < 1 or capacity > 10:
        raise ValueError("Invalid capacity")
    
    count = 0
    for row in grid:
        for well in row:
            count += math.ceil(well / capacity)

    return count
import unittest

class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1), 6)

    def test_example2(self):
        self.assertEqual(max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2), 5)

    def test_example3(self):
        self.assertEqual(max_fill([[0,0,0], [0,0,0]], 5), 0)

if __name__ == '__main__':
    unittest.main()