def count_bidirectional(test_list):
    '''
    Write a function to count bidirectional tuple pairs.
    assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 3
    '''

    bidirectional_pairs_count = 0
    unique_tuples_count = {}
    
    for tup in test_list:
        reverse_tup = tuple(reversed(tup))
        if reverse_tup in unique_tuples_count:
            bidirectional_pairs_count += 1
        else:
            unique_tuples_count[tup] = 1
    
    return bidirectional_pairs_count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)]), 3)

if __name__ == '__main__':
    unittest.main()