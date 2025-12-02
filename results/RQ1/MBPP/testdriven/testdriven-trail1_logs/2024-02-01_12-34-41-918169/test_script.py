def max_length_list(input_list):
    if not isinstance(input_list, list) or not all(isinstance(lst, list) for lst in input_list) or len(input_list) == 0:
        raise ValueError("Input_list must be a non-empty list of lists")

    max_length = max(len(lst) for lst in input_list)

    max_length_lists = [lst for lst in input_list if len(lst) == max_length]

    return max_length, max_length_lists[0]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_length_list([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]), (3, [13, 15, 17]))

if __name__ == '__main__':
    unittest.main()