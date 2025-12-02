def count_no_of_ways(n, k):
    def calculate_ways_dp(n, k):
        # Implementation of dynamic programming technique to optimize calculation
        # write your implementation here
        pass

    def check_adjacent_colors(n):
        # Implementation to check and ensure at most 2 adjacent posts have the same color
        # write your implementation here
        pass

    def unit_tests():
        # Write unit tests to cover different scenarios and edge cases
        # write your implementation here
        pass

    return calculate_ways_dp(n, k), check_adjacent_colors(n), unit_tests()

assert count_no_of_ways(2, 4) == 16
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_no_of_ways(2, 4), 16)

if __name__ == '__main__':
    unittest.main()