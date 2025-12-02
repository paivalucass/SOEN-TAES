def next_smallest(lst):
    if not isinstance(lst, list) or not all(isinstance(i, int) for i in lst):
        raise ValueError("Input must be a list of integers")

    if len(lst) < 2:
        return None

    unique_elements = sorted(set(lst))
    if len(unique_elements) < 2:
        return None

    return unique_elements[1]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(next_smallest([1, 2, 3, 4, 5]), 2)
        self.assertEqual(next_smallest([5, 1, 4, 3, 2]), 2)
        self.assertEqual(next_smallest([]), None)
        self.assertEqual(next_smallest([1, 1]), None)

if __name__ == '__main__':
    unittest.main()