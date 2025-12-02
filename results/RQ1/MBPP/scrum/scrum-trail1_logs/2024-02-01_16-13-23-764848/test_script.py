def swap_List(newList):
    if len(newList) == 0:
        return "Error: Input list is empty"
    elif len(newList) == 1:
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