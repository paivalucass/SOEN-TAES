def get_list_difference(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        return "Input parameters are not lists"
    elif not list1 or not list2:
        return "Input lists are empty"

    diff_list = [item for item in list1 if item not in list2]
    return diff_list

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]), [10, 20, 30, 15])

if __name__ == '__main__':
    unittest.main()