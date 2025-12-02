def extract_freq(test_list):
    freq_map = {}
    for tup in test_list:
        if tup in freq_map:
            freq_map[tup] += 1
        else:
            freq_map[tup] = 1

    unique_count = sum(1 for freq in freq_map.values() if freq == 1)

    return unique_count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)]), 3)

if __name__ == '__main__':
    unittest.main()