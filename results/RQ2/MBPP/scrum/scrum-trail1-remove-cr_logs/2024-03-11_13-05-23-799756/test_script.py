def max_length(list1):
    if not list1:
        return "Input list is empty"

    max_len = 0
    max_list = []

    for sub_list in list1:
        if len(sub_list) > max_len:
            max_len = len(sub_list)
            max_list = sub_list

    return (max_len, max_list)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]), (3, [13, 15, 17]))

if __name__ == '__main__':
    unittest.main()