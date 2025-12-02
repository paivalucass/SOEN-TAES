def strange_sort_list(lst):
    if not lst:
        return []

    if len(set(lst)) != len(lst):
        return 'Error: Input list contains repeated values'

    sorted_lst = sorted(lst)
    result_lst = []
    if len(sorted_lst) == 1:
        result_lst.append(sorted_lst[0])
    else:
        for i in range(0, len(sorted_lst)//2):
            result_lst.append(sorted_lst[i])
            if len(sorted_lst) - i - 1 != i:
                result_lst.append(sorted_lst[-(i+1)])
    return result_lst
import unittest

class Test(unittest.TestCase):
    def test_strange_sort_list(self):
        self.assertEqual(strange_sort_list([1, 2, 3, 4]), [1, 4, 2, 3])
        self.assertEqual(strange_sort_list([5, 5, 5, 5]), [5, 5, 5, 5])
        self.assertEqual(strange_sort_list([]), [])

if __name__ == '__main__':
    unittest.main()