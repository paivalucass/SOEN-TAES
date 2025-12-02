def replace_list(list1, list2):
    if not list1 or not list2:
        raise ValueError("Both list1 and list2 must not be empty")

    if type(list1) != type(list2):
        raise ValueError("Both list1 and list2 must be of the same type")

    if list2:
        list1 = list1[:-1] + list2

    return list1
import unittest

class Test(unittest.TestCase):
    def test_replace_list(self):
        self.assertEqual(replace_list([1, 3, 5, 7, 9, 10], [2, 4, 6, 8]), [1, 3, 5, 7, 9, 2, 4, 6, 8])

if __name__ == '__main__':
    unittest.main()