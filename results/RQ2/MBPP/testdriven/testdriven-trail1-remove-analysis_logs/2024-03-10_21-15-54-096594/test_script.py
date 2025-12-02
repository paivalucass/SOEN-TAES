def max_length(list1):
    max_len = 0
    max_list = []
    for sublist in list1:
        if not isinstance(sublist, list):
            raise TypeError("Input must be a list of lists")
        if len(sublist) > max_len:
            max_len = len(sublist)
            max_list = sublist
    return (max_len, max_list)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]), (3, [13, 15, 17]))

if __name__ == '__main__':
    unittest.main()