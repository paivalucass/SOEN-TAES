def extract_freq(test_list):
    freq_dict = {}
    for item in test_list:
        if not isinstance(item, tuple):
            raise TypeError("Error: Non-tuple element found")
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    unique_tuples = sum(1 for count in freq_dict.values() if count == 1)
    return unique_tuples
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)]), 3)

if __name__ == '__main__':
    unittest.main()