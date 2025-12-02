def extract_freq(test_list):
    freq_set = set(map(tuple, test_list))
    return len(freq_set)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)]), 3)

if __name__ == '__main__':
    unittest.main()