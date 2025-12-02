def strange_sort_list(lst):
    input_list = lst.copy()
    
    def find_min_max(lst):
        return min(lst), max(lst)
    
    result = []
    while input_list:
        min_val, max_val = find_min_max(input_list)
        result.append(min_val)
        input_list.remove(min_val)
        if input_list:
            result.append(max_val)
            input_list.remove(max_val)
    
    return result
import unittest

class Test(unittest.TestCase):
    def test_strange_sort_list(self):
        self.assertEqual(strange_sort_list([1, 2, 3, 4]), [1, 4, 2, 3])
        self.assertEqual(strange_sort_list([5, 5, 5, 5]), [5, 5, 5, 5])
        self.assertEqual(strange_sort_list([]), [])

if __name__ == '__main__':
    unittest.main()