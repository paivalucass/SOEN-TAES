def cummulative_sum(test_list):
    result = []
    cum_sum = 0
    for tuple in test_list:
        cum_sum = sum(tuple)
        result.append(cum_sum)
    return sum(result)
import unittest

class Test(unittest.TestCase):
    def test_cummulative_sum(self):
        self.assertEqual(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]), 30)

if __name__ == '__main__':
    unittest.main()