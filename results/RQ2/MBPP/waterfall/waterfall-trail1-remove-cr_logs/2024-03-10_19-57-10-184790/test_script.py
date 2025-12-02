def replace_list(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Input should be lists")

    if not list1 or not list2:
        raise ValueError("Input lists should not be empty")

    if not all(isinstance(x, int) for x in list1[:-1]):
        raise ValueError("Elements in the first list should be integers")

    list1[-1:] = list2
    return list1
import unittest

class Test(unittest.TestCase):
    def test_replace_list(self):
        self.assertEqual(replace_list([1, 3, 5, 7, 9, 10],[2, 4, 6, 8]), [1, 3, 5, 7, 9, 2, 4, 6, 8])

if __name__ == '__main__':
    unittest.main()