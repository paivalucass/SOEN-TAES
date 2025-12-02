def max_length_list(input_list):
    max_length = 0
    max_length_list = []
    for sub_list in input_list:
        if len(sub_list) > max_length:
            max_length = len(sub_list)
            max_length_list = sub_list
    return max_length, max_length_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_length_list([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]), (3, [13, 15, 17]))

if __name__ == '__main__':
    unittest.main()