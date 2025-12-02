def cumulative_sum(test_list):
    '''Write a function to find the cumulative sum of all the values that are present in the given tuple list.'''
    total_sum = 0
    for tup in test_list:
        total_sum += sum(tup)
    return total_sum

assert cumulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]), 30)

if __name__ == '__main__':
    unittest.main()