def sort_even(l: list):
    for i in range(0, len(l), 2):
        for j in range(i+2, len(l), 2):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    return l
import unittest

class Test(unittest.TestCase):
    def test_sort_even(self):
        self.assertEqual(sort_even([1, 2, 3]), [1, 2, 3])
        self.assertEqual(sort_even([5, 6, 3, 4]), [3, 6, 5, 4])

if __name__ == '__main__':
    unittest.main()