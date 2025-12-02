def count_bidirectional(test_list):
    count = 0
    pair_map = {}
    for pair in test_list:
        if pair[1] in pair_map and pair_map[pair[1]] == pair[0]:
            count += 1
        else:
            pair_map[pair[0]] = pair[1]
    return count
import unittest

class Test(unittest.TestCase):
    def test_count_bidirectional(self):
        self.assertEqual(count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)]), 3)

if __name__ == '__main__':
    unittest.main()