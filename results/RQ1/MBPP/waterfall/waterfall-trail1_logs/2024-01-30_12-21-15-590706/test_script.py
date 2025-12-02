def max_difference(pair_list):
    for pair in pair_list:
        if not isinstance(pair, tuple) or len(pair) != 2:
            raise ValueError("Input list should contain tuples with exactly two elements")
    
    max_diff = 0
    for pair in pair_list:
        diff = abs(pair[0] - pair[1])
        if diff > max_diff:
            max_diff = diff
    
    return max_diff
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]), 7)

if __name__ == '__main__':
    unittest.main()