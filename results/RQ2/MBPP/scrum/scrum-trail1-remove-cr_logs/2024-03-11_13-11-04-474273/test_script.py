def max_length_list(input_list):
    if not input_list or not any(isinstance(i, list) for i in input_list):
        raise ValueError("Input_list is empty or does not contain any lists")

    max_length = 0
    max_list = []
    for lst in input_list:
        if len(lst) > max_length:
            max_length = len(lst)
            max_list = lst
    
    return max_length, max_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_length_list([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]), (3, [13, 15, 17]))

if __name__ == '__main__':
    unittest.main()