def cumulative_sum(test_list):
    result = 0
    for sub_tuple in test_list:
        result += sum(sub_tuple)
    return result
import unittest

class Test(unittest.TestCase):
    def test_cummulative_sum(self):
        self.assertEqual(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]), 30)

if __name__ == '__main__':
    unittest.main()