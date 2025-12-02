def count_bidirectional(test_list):
    count = 0
    seen_pairs = set()
    for pair in test_list:
        if (pair[1], pair[0]) in seen_pairs:
            count += 1
        seen_pairs.add(pair)
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)]), 3)

if __name__ == '__main__':
    unittest.main()