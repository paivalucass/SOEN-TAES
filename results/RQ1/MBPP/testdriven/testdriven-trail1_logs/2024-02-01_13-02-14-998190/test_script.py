def swap_List(newList):
    '''Write a python function to interchange the first and last elements in a list.
    assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]'''

    # Error handling for invalid input list type
    if not isinstance(newList, list):
        return "Invalid input: not a list type"

    # Test cases for different types of input lists
    if len(newList) < 1:
        return "Input list is empty"
    else:
        newList[0], newList[-1] = newList[-1], newList[0]
        return newList
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(swap_List([12, 35, 9, 56, 24]), [24, 35, 9, 56, 12])

if __name__ == '__main__':
    unittest.main()