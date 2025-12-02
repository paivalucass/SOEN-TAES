def is_sorted(lst):
    if len(lst) < 2:
        return True
    for i in range(len(lst) - 1):
        if lst[i] >= lst[i+1] or lst.count(lst[i]) > 1:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_sorted([5]), True)
        self.assertEqual(is_sorted([1, 2, 3, 4, 5]), True)
        self.assertEqual(is_sorted([1, 3, 2, 4, 5]), False)
        self.assertEqual(is_sorted([1, 2, 3, 4, 5, 6]), True)
        self.assertEqual(is_sorted([1, 2, 3, 4, 5, 6, 7]), True)
        self.assertEqual(is_sorted([1, 3, 2, 4, 5, 6, 7]), False)
        self.assertEqual(is_sorted([1, 2, 2, 3, 3, 4]), True)
        self.assertEqual(is_sorted([1, 2, 2, 2, 3, 4]), False)

if __name__ == '__main':
    unittest.main()