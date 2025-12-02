def count_bidirectional(test_list):
    '''This function counts bidirectional tuple pairs.'''
    pair_count = 0
    pair_dict = {}

    for pair in test_list:
        if pair in pair_dict:
            pair_count += pair_dict[pair]
            pair_dict[pair] += 1
        else:
            reverse_pair = (pair[1], pair[0])
            if reverse_pair in pair_dict and pair_dict[reverse_pair] > 0:
                pair_count += 1
                pair_dict[reverse_pair] -= 1
            else:
                pair_dict[pair] = 1

    return pair_count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)]), 3)

if __name__ == '__main__':
    unittest.main()