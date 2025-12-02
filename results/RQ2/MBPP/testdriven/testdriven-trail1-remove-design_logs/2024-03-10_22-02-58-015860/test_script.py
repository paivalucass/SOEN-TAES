def split_two_parts(input_list, L):
    '''
    This function takes in a list and an integer L and splits the given list into two parts where the length of the first part of the list is L, and returns the resulting lists in a tuple.
    '''

    if not isinstance(L, int) or L < 0:
        return "Invalid input"

    if L >= len(input_list):
        return (input_list, [])

    return (input_list[:L], input_list[L:])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(split_two_parts([1,1,2,3,4,4,5,1], 3), ([1, 1, 2], [3, 4, 4, 5, 1]))

if __name__ == '__main__':
    unittest.main()