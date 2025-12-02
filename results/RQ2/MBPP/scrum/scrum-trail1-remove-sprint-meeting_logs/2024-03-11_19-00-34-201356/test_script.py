def swap_List(newList):
    if isinstance(newList, list) and all(isinstance(x, int) for x in newList):
        if newList:
            newList[0], newList[-1] = newList[-1], newList[0]
        return newList
    return "Input is not a list of integers or the list is empty"
import unittest

class Test(unittest.TestCase):
    def test_swap_List(self):
        self.assertEqual(swap_List([1,2,3]), [3,2,1])

if __name__ == '__main__':
    unittest.main()