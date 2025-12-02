def max_difference(test_list):
    if len(test_list) < 2:
        return 0
    
    max_diff = 0
    for tuple_pair in test_list:
        diff = abs(tuple_pair[0] - tuple_pair[1])
        if diff > max_diff:
            max_diff = diff
    
    return max_diff
import unittest

class Test(unittest.TestCase):
    def test_max_difference(self):
        self.assertEqual(max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]), 7)

if __name__ == '__main__':
    unittest.main()