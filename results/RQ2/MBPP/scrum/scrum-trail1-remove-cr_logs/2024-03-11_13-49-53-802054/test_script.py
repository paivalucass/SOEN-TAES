def swap_List(newList):
    if not isinstance(newList, list):
        return "Error: Input is not a valid list"

    if len(newList) < 2:
        return "Error: List must have at least two elements"

    first_element = newList[0]
    last_element = newList[-1]

    newList[0] = last_element
    newList[-1] = first_element

    return newList
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(swap_List([1,2,3]), [3,2,1])

if __name__ == '__main__':
    unittest.main()