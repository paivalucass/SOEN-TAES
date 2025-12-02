def max_length(list1):
    if not list1 or not all(isinstance(sub_list, list) for sub_list in list1):
        raise ValueError("Input list should not be empty and should only contain lists.")

    max_len = 0
    longest_list = []
    for sub_list in list1:
        if len(sub_list) > max_len:
            max_len = len(sub_list)
            longest_list = sub_list
    return (max_len, longest_list)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]), (3, [13, 15, 17]))

if __name__ == '__main__':
    unittest.main()