def count_bidirectional(test_list):
    pair_set = set()
    count = 0
    for pair in test_list:
        reverse_pair = (pair[1], pair[0])
        if pair in pair_set or reverse_pair in pair_set:
            count += 1
        pair_set.add(pair)
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)]), 3)

if __name__ == '__main__':
    unittest.main()