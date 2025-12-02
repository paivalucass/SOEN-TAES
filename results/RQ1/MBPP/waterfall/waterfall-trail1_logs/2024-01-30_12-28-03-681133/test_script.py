def frequency_lists(list_of_lists):
    if not isinstance(list_of_lists, list):
        raise TypeError("Input must be a list of lists")

    flattened_list = [item for sublist in list_of_lists for item in sublist]
    frequency_dict = {}
    for item in flattened_list:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    return frequency_dict
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]), {1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1})

if __name__ == '__main__':
    unittest.main()