def swap_List(newList):
    if not isinstance(newList, list):
        raise ValueError("Input should be a list")
    
    if len(newList) <= 1:
        raise ValueError("List should have at least two elements")

    newList[0], newList[-1] = newList[-1], newList[0]

    return newList
import unittest

class Test(unittest.TestCase):
    def test_swap_List(self):
        self.assertEqual(swap_List([12, 35, 9, 56, 24]), [24, 35, 9, 56, 12])

if __name__ == '__main__':
    unittest.main()