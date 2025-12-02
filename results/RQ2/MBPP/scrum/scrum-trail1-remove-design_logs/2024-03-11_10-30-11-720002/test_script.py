def max_length_list(input_list):
    max_length = 0
    max_length_index = 0
    for i in range(len(input_list)):
        if len(input_list[i]) >= max_length:
            max_length = len(input_list[i])
            max_length_index = i
    return max_length_index, input_list[max_length_index]
import unittest

class TestMaxListLength(unittest.TestCase):
    def test_max_length_list(self):
        self.assertEqual(max_length_list([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]), (3, [13, 15, 17]))

if __name__ == '__main__':
    unittest.main()