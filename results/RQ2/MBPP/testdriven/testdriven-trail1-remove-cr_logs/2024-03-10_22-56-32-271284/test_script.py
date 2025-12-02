def extract_freq(test_list):
    if not isinstance(test_list, list):
        return "Invalid input"
    
    unique_tuples = set([tuple(sorted(t)) for t in test_list])
    return len(unique_tuples)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)]), 3)

if __name__ == '__main__':
    unittest.main()