from typing import List

def swap_List(newList: List) -> List:
    if len(newList) <= 1:
        raise ValueError("List should have at least two elements")
    else:
        newList[0], newList[-1] = newList[-1], newList[0]
        return newList

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(swap_List([1,2,3]), [3,2,1])

if __name__ == '__main__':
    unittest.main()