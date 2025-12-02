def split_two_parts(list1, L):
    '''Write a function that takes in a list and an integer L and splits the given list into two parts where the length of the first part of the list is L, and returns the resulting lists in a tuple.'''
    if type(list1) != list or len(list1) == 0:
        raise ValueError("Input list is invalid or empty")

    if type(L) != int or L < 0:
        raise ValueError("L should be a non-negative integer")

    if L > len(list1):
        raise ValueError("L should be less than or equal to the length of the input list")

    first_part = list1[:L]
    second_part = list1[L:]
    return (first_part, second_part)

assert split_two_parts([1,1,2,3,4,4,5,1],3)==([1, 1, 2], [3, 4, 4, 5, 1])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(split_two_parts([1,1,2,3,4,4,5,1], 3), ([1, 1, 2], [3, 4, 4, 5, 1]))

if __name__ == '__main__':
    unittest.main()