def max_difference(test_list):
    if len(test_list) < 2:
        return "Error: test_list must contain at least two elements"
    
    max_diff = 0
    for pair in test_list:
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