def cumulative_sum(test_list):
    '''Write a function to find the cumulative sum of all the values that are present in the given tuple list.'''
    if not isinstance(test_list, list) or not all(isinstance(t, tuple) for t in test_list):
        raise ValueError("Input must be a list of tuples")

    return sum(sum(t) for t in test_list)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]), 30)

if __name__ == '__main__':
    unittest.main()