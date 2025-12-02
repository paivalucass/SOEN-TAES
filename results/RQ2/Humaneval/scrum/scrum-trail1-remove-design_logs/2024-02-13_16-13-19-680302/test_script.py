def next_smallest(lst):
    sorted_list = sorted(set(lst))
    if len(sorted_list) < 2:
        return None
    else:
        return sorted_list[1]
import unittest

class Test(unittest.TestCase):
    def test_next_smallest(self):
        self.assertEqual(next_smallest([1, 2, 3, 4, 5]), 2)
        self.assertEqual(next_smallest([5, 1, 4, 3, 2]), 2)
        self.assertIsNone(next_smallest([]))
        self.assertIsNone(next_smallest([1, 1])

if __name__ == '__main__':
    unittest.main()