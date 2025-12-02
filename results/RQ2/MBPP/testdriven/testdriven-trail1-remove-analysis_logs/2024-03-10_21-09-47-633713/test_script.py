def frequency_lists(list1):
    from collections import Counter
    flattened_list = [item for sublist in list1 for item in sublist]
    return dict(Counter(flattened_list))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]), {1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1})

if __name__ == '__main__':
    unittest.main()