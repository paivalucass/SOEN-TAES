def max_length_list(input_list):
    if not isinstance(input_list, list) or len(input_list) == 0:
        return 'Invalid input list'

    max_length = 0
    max_length_sublists = []
    for sublist in input_list:
        if not isinstance(sublist, list):
            return 'Invalid input list'
        if len(sublist) > max_length:
            max_length = len(sublist)
            max_length_sublists = [sublist]
        elif len(sublist) == max_length:
            max_length_sublists.append(sublist)

    return (max_length, max_length_sublists)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_length_list([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]), (3, [13, 15, 17]))

if __name__ == '__main__':
    unittest.main()