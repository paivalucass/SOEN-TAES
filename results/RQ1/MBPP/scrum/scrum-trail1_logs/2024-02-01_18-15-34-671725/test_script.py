def swap_List(newList):
    if newList is None or not isinstance(newList, list):
        raise ValueError("Input must be a non-empty list.")

    if len(newList) <= 1:
        return newList

    newList[0], newList[-1] = newList[-1], newList[0]

    return newList
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(swap_List([1,2,3]), [3,2,1])

if __name__ == '__main__':
    unittest.main()