def frequency_lists(list1):
    from collections import Counter
    if not list1 or any(isinstance(sublist, list) for sublist in list1):
        return {}
    try:
        flat_list = [item for sublist in list1 for item in sublist]
        frequency_dict = dict(Counter(flat_list))
        return frequency_dict
    except TypeError:
        return "Non-hashable elements found in the list"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]), {1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1})

if __name__ == '__main__':
    unittest.main()