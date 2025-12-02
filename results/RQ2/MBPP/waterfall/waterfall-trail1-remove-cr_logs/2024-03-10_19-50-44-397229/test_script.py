def max_difference(test_list):
    if len(test_list) < 2:
        return 0
    max_diff = 0
    min_val = float('inf')
    max_val = float('-inf')
    
    for pair in test_list:
        min_val = min(pair[0], min_val)
        max_val = max(pair[1], max_val)
        max_diff = max(max_diff, max_val - min_val)
    
    return max_diff
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]), 7)

if __name__ == '__main__':
    unittest.main()