def max_length(list1):
    max_length = 0
    max_list = []
    for sublist in list1:
        if len(sublist) > max_length:
            max_length = len(sublist)
            max_list = sublist
    return (max_length, max_list)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]), (3, [13, 15, 17]))

if __name__ == '__main__':
    unittest.main()