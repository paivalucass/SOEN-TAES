def count_bidirectional(test_list):
    reversed_pairs = set()
    count = 0
    for pair in test_list:
        if not isinstance(pair, tuple):
            return "Error: Input elements must be tuples"
        reversed_pair = (pair[1], pair[0])
        if reversed_pair in reversed_pairs:
            count += 1
        else:
            reversed_pairs.add(pair)
    return count 
import unittest

class Test(unittest.TestCase):
    def test_count_bidirectional(self):
        self.assertEqual(count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)]), 3)

if __name__ == '__main__':
    unittest.main()