def is_sorted(lst):
    if len(lst) <= 1:
        return True
    prev = lst[0]
    count = 1
    for num in lst[1:]:
        if num < prev or (num == prev and count >= 2):
            return False
        if num == prev:
            count += 1
        else:
            count = 1
        prev = num
    return True
import unittest

class Test(unittest.TestCase):
    def test_is_sorted(self):
        self.assertEqual(is_sorted([5]), True)
        self.assertEqual(is_sorted([1, 2, 3, 4, 5]), True)
        self.assertEqual(is_sorted([1, 3, 2, 4, 5]), False)
        self.assertEqual(is_sorted([1, 2, 3, 4, 5, 6]), True)
        self.assertEqual(is_sorted([1, 2, 3, 4, 5, 6, 7]), True)
        self.assertEqual(is_sorted([1, 3, 2, 4, 5, 6, 7]), False)
        self.assertEqual(is_sorted([1, 2, 2, 3, 3, 4]), True)
        self.assertEqual(is_sorted([1, 2, 2, 2, 3, 4]), False)

if __name__ == '__main__':
    unittest.main()