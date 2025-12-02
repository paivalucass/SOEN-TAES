def strange_sort_list(lst):
    sorted_lst = sorted(lst)
    new_lst = []
    for i in range(len(sorted_lst)):
        if i % 2 == 0:
            new_lst.append(sorted_lst[i])
        else:
            new_lst.insert(1, sorted_lst[i])
    return new_lst

import unittest

class Test(unittest.TestCase):
    def test_strange_sort_list(self):
        self.assertEqual(strange_sort_list([1, 2, 3, 4]), [1, 4, 2, 3])
        self.assertEqual(strange_sort_list([5, 5, 5, 5]), [5, 5, 5, 5])
        self.assertEqual(strange_sort_list([]), [])

if __name__ == '__main__':
    unittest.main()