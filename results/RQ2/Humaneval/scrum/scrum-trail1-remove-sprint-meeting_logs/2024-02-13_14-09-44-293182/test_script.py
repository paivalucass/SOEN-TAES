def next_smallest(lst):
    if not isinstance(lst, list) or not all(isinstance(x, int) for x in lst):
        return "Error: Input is not a list of integers"
    elif len(lst) <= 1:
        return None
    unique_elements = list(set(lst)) 
    if len(unique_elements) < 2:
        return None
    else:
        return sorted(unique_elements)[1]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(next_smallest([1, 2, 3, 4, 5]), 2)
        self.assertEqual(next_smallest([5, 1, 4, 3, 2]), 2)
        self.assertIsNone(next_smallest([]))
        self.assertIsNone(next_smallest([1, 1]))

if __name__ == '__main__':
    unittest.main()