def frequency_lists(list1):
    if not list1:
        raise ValueError("Input list cannot be empty")
    if not all(isinstance(sublist, list) for sublist in list1):
        raise ValueError("Input must be a list of lists")

    frequency_dict = {}

    for sublist in list1:
        for element in sublist:
            if element in frequency_dict:
                frequency_dict[element] += 1
            else:
                frequency_dict[element] = 1

    return frequency_dict
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]), {1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1})

if __name__ == '__main__':
    unittest.main()