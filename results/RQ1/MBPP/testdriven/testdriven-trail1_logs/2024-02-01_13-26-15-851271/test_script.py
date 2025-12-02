def find_list_difference(list1, list2):
    if list1 is None or list2 is None:
        return "Error: Input lists cannot be None"
    if not isinstance(list1, list) or not isinstance(list2, list):
        return "Error: Input is not a list"
    difference = [item for item in list1 if item not in list2]
    return difference
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]), [10, 20, 30, 15])

if __name__ == '__main__':
    unittest.main()