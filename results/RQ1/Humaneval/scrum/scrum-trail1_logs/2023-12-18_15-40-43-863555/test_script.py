import math

def max_fill(grid, capacity):
    def calculate_total_water(row):
        return sum(row)
    
    def determine_number_of_buckets(total_water, capacity):
        return math.ceil(total_water / capacity)
    
    if not grid or capacity <= 0:
        return 0
    
    total_buckets_lowered = 0
    for row in grid:
        total_water = calculate_total_water(row)
        total_buckets_lowered += determine_number_of_buckets(total_water, capacity)
    
    return total_buckets_lowered
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