def swap_List(newList):
    if not isinstance(newList, list):
        return "Input must be a list"
    if len(newList) < 2:
        return "Input list must have at least two elements"
    else:
        newList[0], newList[-1] = newList[-1], newList[0]
        return newList
import unittest

class Test(unittest.TestCase):
    def test_swap_List(self):
        self.assertEqual(swap_List([1,2,3]), [3,2,1])

if __name__ == '__main__':
    unittest.main()