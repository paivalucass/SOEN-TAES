def extract_freq(test_list):
    if not isinstance(test_list, list) or len(test_list) == 0:
        raise ValueError("Input list is empty or not a valid list")

    unique_tuples = set()
    for item in test_list:
        unique_tuples.add(tuple(sorted(item)))
    return len(unique_tuples)
import unittest

class Test(unittest.TestCase):
    def test_extract_freq(self):
        self.assertEqual(extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)]), 3)

if __name__ == '__main__':
    unittest.main()