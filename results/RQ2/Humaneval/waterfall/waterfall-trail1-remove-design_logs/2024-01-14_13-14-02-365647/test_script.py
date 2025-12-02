def next_smallest(lst):
    if len(lst) < 2:
        return None
    else:
        unique_lst = list(set(lst))
        if len(unique_lst) < 2:
            return None
        else:
            unique_lst.sort()
            return unique_lst[1]
import unittest

class Test(unittest.TestCase):
    def test_next_smallest(self):
        self.assertEqual(next_smallest([1, 2, 3, 4, 5]), 2)
        self.assertEqual(next_smallest([5, 1, 4, 3, 2]), 2)
        self.assertEqual(next_smallest([]), None)
        self.assertEqual(next_smallest([1, 1]), None)

if __name__ == '__main__':
    unittest.main()