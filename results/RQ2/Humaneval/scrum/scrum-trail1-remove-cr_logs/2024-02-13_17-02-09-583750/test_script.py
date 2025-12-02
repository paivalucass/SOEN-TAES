def strange_sort_list(lst):
    if not lst:
        return []

    sorted_list = []
    lst.sort()

    while lst:
        sorted_list.append(lst.pop(0))
        if lst:
            sorted_list.append(lst.pop(-1))

    return sorted_list
import unittest

class Test(unittest.TestCase):
    def test_strange_sort_list(self):
        self.assertEqual(strange_sort_list([1, 2, 3, 4]), [1, 4, 2, 3])
        self.assertEqual(strange_sort_list([5, 5, 5, 5]), [5, 5, 5, 5])
        self.assertEqual(strange_sort_list([]), [])

if __name__ == '__main__':
    unittest.main()