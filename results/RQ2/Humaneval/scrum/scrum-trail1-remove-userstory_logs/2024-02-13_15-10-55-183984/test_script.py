from collections import Counter

def search(lst):
    freq_map = Counter(lst)
    max_val = -1
    for num, freq in freq_map.items():
        if num > 0 and freq >= num:
            max_val = max(max_val, num)
    return max_val
import unittest

class Test(unittest.TestCase):
    def test_search_1(self):
        self.assertEqual(search([4, 1, 2, 2, 3, 1]), 2)

    def test_search_2(self):
        self.assertEqual(search([1, 2, 2, 3, 3, 3, 4, 4, 4]), 3)

    def test_search_3(self):
        self.assertEqual(search([5, 5, 4, 4, 4]), -1)

if __name__ == '__main__':
    unittest.main()