def swap_List(newList):
    if len(newList) < 2:
        raise ValueError("Input list must have at least two elements")

    newList[0], newList[-1] = newList[-1], newList[0]
    return newList

assert swap_List([1,2,3]) == [3,2,1]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(swap_List([1,2,3]), [3,2,1])

if __name__ == '__main__':
    unittest.main()