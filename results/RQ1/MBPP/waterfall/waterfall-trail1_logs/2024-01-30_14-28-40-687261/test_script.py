def count_bidirectional(test_list):
    if not test_list or any(len(t) != 2 for t in test_list):
        return 0

    count_dict = {}
    count = 0
    for tup in test_list:
        reverse_tup = (tup[1], tup[0])
        if reverse_tup in count_dict:
            count += 1
        count_dict[tup] = count_dict.get(tup, 0) + 1

    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)]), 3)

if __name__ == '__main__':
    unittest.main()