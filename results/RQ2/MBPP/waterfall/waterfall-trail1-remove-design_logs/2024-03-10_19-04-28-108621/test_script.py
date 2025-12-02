def max_difference(test_list):
    if not all(isinstance(item, tuple) and len(item) == 2 for item in test_list):
        raise ValueError("test_list should contain pairs of numbers")
    
    max_diff = 0
    for pair in test_list:
        difference = abs(pair[0] - pair[1])
        if difference > max_diff:
            max_diff = difference
    return max_diff
import unittest

class Test(unittest.TestCase):
    def test_max_difference(self):
        self.assertEqual(max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]), 7)

if __name__ == '__main__':
    unittest.main()