def extract_singly(test_list):
    for inner_list in test_list:
        if not isinstance(inner_list, list) or not all(isinstance(num, (int, float)) for num in inner_list):
            raise TypeError("Input must be a list of lists and each inner list should only contain numbers.")
    flattened_list = [num for inner_list in test_list for num in inner_list]
    return set(flattened_list)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)]), set([3, 4, 5, 7, 1]))

if __name__ == '__main__':
    unittest.main()