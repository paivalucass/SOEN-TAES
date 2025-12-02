def max_length_list(input_list):
    if not isinstance(input_list, list) or not all(isinstance(sublist, list) for sublist in input_list):
        raise ValueError("Input must be a list of lists")

    max_length = 0
    max_length_sublist = []

    for sublist in input_list:
        if len(sublist) > max_length:
            max_length = len(sublist)
            max_length_sublist = sublist

    return (max_length, max_length_sublist)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_length_list([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]), (3, [13, 15, 17]))

if __name__ == '__main__':
    unittest.main()