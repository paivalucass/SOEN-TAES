import math

def max_fill(grid, capacity):
    total_times_lower_buckets = 0
    
    for row in grid:
        total_units = sum(row)
        times_lower_bucket = math.ceil(total_units / capacity)
        total_times_lower_buckets += times_lower_bucket
    
    return total_times_lower_buckets
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