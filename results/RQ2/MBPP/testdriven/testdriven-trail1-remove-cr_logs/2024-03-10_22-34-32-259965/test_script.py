def replace_list(list1, list2):
    if list2 is None:
        return "Error: Second list is null"
    else:
        list1 = list1[:-1] + list2
        return list1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_list([1, 3, 5, 7, 9, 10], [2, 4, 6, 8]), [1, 3, 5, 7, 9, 2, 4, 6, 8])

if __name__ == '__main__':
    unittest.main()