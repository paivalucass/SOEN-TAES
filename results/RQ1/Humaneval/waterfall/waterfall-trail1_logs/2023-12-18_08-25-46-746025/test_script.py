import math

def max_fill(grid, capacity):
    if not isinstance(grid, list) or not all(isinstance(row, list) and len(row) == len(grid[0]) for row in grid):
        raise ValueError("Invalid grid input: grid must be a rectangular list of lists")
    if not isinstance(capacity, int) or capacity < 1 or capacity > 10:
        raise ValueError("Invalid bucket capacity input: capacity must be an integer between 1 and 10")
    
    total_water = sum(sum(row) for row in grid)
    buckets_needed = math.ceil(total_water / capacity)
    return buckets_needed
import math

class Test(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1), 6)

    def test_case2(self):
        self.assertEqual(max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2), 5)

    def test_case3(self):
        self.assertEqual(max_fill([[0,0,0], [0,0,0]], 5), 0)

if __name__ == '__main__':
    unittest.main()