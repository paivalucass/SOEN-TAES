def replace_list(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        return "Invalid input: both list1 and list2 must be lists"
    if not list1 or not list2:
        return "Invalid input: both list1 and list2 must not be empty"
    if len(list1) < len(list2):
        return "Invalid input: list2 must not be longer than list1"
    list1 = list1[:-len(list2)] + list2
    return list1
import unittest

class Test(unittest.TestCase):
    def test_replace_list(self):
        self.assertEqual(replace_list([1, 3, 5, 7, 9, 10], [2, 4, 6, 8]), [1, 3, 5, 7, 9, 2, 4, 6, 8])

if __name__ == '__main__':
    unittest.main()