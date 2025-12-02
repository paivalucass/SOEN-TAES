def max_length_list(input_list):
    if not isinstance(input_list, list):
        return None
    if not input_list:
        return None
    max_length = 0
    max_length_lists = []
    for lst in input_list:
        if isinstance(lst, list):
            if len(lst) > max_length:
                max_length = len(lst)
                max_length_lists = lst
            elif len(lst) == max_length:
                max_length_lists.append(lst)
    return (max_length, max_length_lists)

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_length_list([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]), (3, [13, 15, 17]))

if __name__ == '__main__':
    unittest.main()