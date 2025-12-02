def extract_freq(test_list):
    freq_dict = {}
    if not all(isinstance(tup, tuple) for tup in test_list):
        return "Error: Input list should only contain tuples"
    for tup in test_list:
        freq_dict[tup] = freq_dict.get(tup, 0) + 1
    return len(set(test_list))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)]), 3)

if __name__ == '__main__':
    unittest.main()