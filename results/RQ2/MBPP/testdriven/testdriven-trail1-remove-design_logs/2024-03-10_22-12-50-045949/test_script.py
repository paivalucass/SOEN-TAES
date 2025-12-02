def swap_List(newList):
    '''
    Write a python function to interchange the first and last elements in a list.
    assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
    '''
    # Swap the first and last elements of the list
    if len(newList) < 2:
        return newList
    else:
        newList[0], newList[-1] = newList[-1], newList[0]
        return newList
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(swap_List([12, 35, 9, 56, 24]), [24, 35, 9, 56, 12])

if __name__ == '__main__':
    unittest.main()