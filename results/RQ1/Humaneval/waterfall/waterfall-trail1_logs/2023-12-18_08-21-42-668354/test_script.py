def next_smallest(lst):
    if len(lst) < 2 or len(set(lst)) < 2:
        return None
    else:
        unique_lst = list(set(lst))
        unique_lst.sort()
        return unique_lst[1]
import unittest

class Test(unittest.TestCase):
    def test_next_smallest(self):
        self.assertEqual(next_smallest([1, 2, 3, 4, 5]), 2)
        self.assertEqual(next_smallest([5, 1, 4, 3, 2]), 2)
        self.assertIsNone(next_smallest([]))
        self.assertIsNone(next_smallest([1, 1]))

if __name__ == '__main__':
    unittest.main()