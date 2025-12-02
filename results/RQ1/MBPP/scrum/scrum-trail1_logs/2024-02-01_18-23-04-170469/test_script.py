def extract_freq(test_list):
    if not test_list or not all(isinstance(item, tuple) for item in test_list):
        return 0
    
    unique_tuples = set(test_list)
    return len(unique_tuples)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)]), 3)

if __name__ == '__main__':
    unittest.main()