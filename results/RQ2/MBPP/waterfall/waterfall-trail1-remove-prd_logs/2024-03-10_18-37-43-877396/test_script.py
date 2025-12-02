def count_element_in_list(list1, x):
    if not isinstance(list1, list):
        raise ValueError("Input is not a list")
    if not all(isinstance(sublist, list) for sublist in list1):
        raise ValueError("All elements in the list should be lists")
    if not isinstance(x, int):
        raise ValueError("Element should be an integer")

    count = sum(1 for sublist in list1 if x in sublist)
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 1), 3)

if __name__ == '__main__':
    unittest.main()