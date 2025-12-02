def next_smallest(lst):
    if len(lst) < 2:
        return None
    else:
        unique_sorted_lst = sorted(set(lst))
        return unique_sorted_lst[1] if len(unique_sorted_lst) > 1 else None
import unittest

class Test(unittest.TestCase):
    def test_next_smallest(self):
        self.assertEqual(next_smallest([1, 2, 3, 4, 5]), 2)
        self.assertEqual(next_smallest([5, 1, 4, 3, 2]), 2)
        self.assertEqual(next_smallest([]), None)
        self.assertEqual(next_smallest([1, 1]), None)

if __name__ == '__main__':
    unittest.main()