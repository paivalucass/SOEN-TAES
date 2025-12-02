def extract_freq(test_list):
    unique_tuple_freq = {}
    for item in test_list:
        if item in unique_tuple_freq:
            unique_tuple_freq[item] += 1
        else:
            unique_tuple_freq[item] = 1
    return len(unique_tuple_freq.keys())
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)]), 3)

if __name__ == '__main__':
    unittest.main()