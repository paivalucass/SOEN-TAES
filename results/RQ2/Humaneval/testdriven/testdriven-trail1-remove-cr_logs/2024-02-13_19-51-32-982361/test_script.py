def is_sorted(lst):
    if not isinstance(lst, list) or not all(isinstance(x, int) for x in lst):
        return "Invalid input"

    prev = lst[0]
    for i in range(1, len(lst)):
        if lst[i] <= prev:
            return False
        prev = lst[i]

    if len(set(lst)) != len(lst):
        return False

    return True
import unittest

class Test(unittest.TestCase):

    def test_is_sorted(self):
        self.assertEqual(is_sorted([5]), True)
        self.assertEqual(is_sorted([1, 2, 3, 4, 5]), True)
        self.assertEqual(is_sorted([1, 3, 2, 4, 5]), False)
        self.assertEqual(is_sorted([1, 2, 3, 4, 5, 6]), True)
        self.assertEqual(is_sorted([1, 2, 2, 3, 3, 4]), True)
        self.assertEqual(is_sorted([1, 2, 2, 2, 3, 4]), False)

if __name__ == '__main__':
    unittest.main()