def max_length_list(input_list):
    longest_length = 0
    longest_list = []
    
    for lst in input_list:
        if len(lst) > longest_length:
            longest_length = len(lst)
            longest_list = lst
    
    return (longest_length, longest_list)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_length_list([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]), (3, [13, 15, 17]))

if __name__ == '__main__':
    unittest.main()