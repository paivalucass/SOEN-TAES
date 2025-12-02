def count_bidirectional(test_list):
    bidirectional_count = 0
    bidirectional_pairs = {}

    for pair in test_list:
        reverse_pair = (pair[1], pair[0])
        if pair in bidirectional_pairs or reverse_pair in bidirectional_pairs:
            bidirectional_count += 1
            if pair in bidirectional_pairs:
                bidirectional_pairs[pair] += 1
            else:
                bidirectional_pairs[reverse_pair] += 1
        else:
            bidirectional_pairs[pair] = 1

    return bidirectional_count
import unittest

class Test(unittest.TestCase):

    def test_count_bidirectional(self):
        self.assertEqual(count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)]), 3)

if __name__ == '__main__':
    unittest.main()