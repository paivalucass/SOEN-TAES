def max_length(list1):
    max_len = 0
    max_list = []
    for l in list1:
        if len(l) > max_len:
            max_len = len(l)
            max_list = l
    return (max_len, max_list)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]), (3, [13, 15, 17]))

if __name__ == '__main__':
    unittest.main()