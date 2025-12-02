def cumulative_sum(test_list):
    if not test_list:
        return "Error: Empty input"
    
    for tup in test_list:
        if any(val < 0 for val in tup):
            return "Error: Negative values not allowed"
    
    result = 0
    for tup in test_list:
        result += sum(tup)
    
    return result
import unittest

class Test(unittest.TestCase):
    def test_cummulative_sum(self):
        self.assertEqual(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]), 30)

if __name__ == '__main__':
    unittest.main()