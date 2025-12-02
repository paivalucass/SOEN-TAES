def strange_sort_list(lst):
    if len(lst) == 0:
        return lst

    sorted_lst = sorted(lst)
    result = []

    for i in range(len(lst) // 2):
        result.append(sorted_lst[i])
        result.append(sorted_lst[-(i + 1)])

    if len(lst) % 2 != 0:
        result.append(sorted_lst[len(lst) // 2])

    return result
import unittest

class Test(unittest.TestCase):
    def test_strange_sort_list(self):
        self.assertEqual(strange_sort_list([1, 2, 3, 4]), [1, 4, 2, 3])
        self.assertEqual(strange_sort_list([5, 5, 5, 5]), [5, 5, 5, 5])
        self.assertEqual(strange_sort_list([]), [])

if __name__ == '__main__':
    unittest.main()