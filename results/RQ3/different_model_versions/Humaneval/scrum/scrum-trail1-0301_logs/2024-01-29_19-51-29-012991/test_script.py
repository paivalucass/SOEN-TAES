def sort_third(l: list):
    l_new = l.copy()
    indices = [i for i in range(len(l_new)) if i % 3 == 0]
    values = [l_new[i] for i in indices]
    values.sort()
    for i in indices:
        l_new[i] = values.pop(0)
    return l_new
import unittest

class Test(unittest.TestCase):
    
    def test_sort_third(self):
        self.assertEqual(sort_third([1, 2, 3]), [1, 2, 3])
        self.assertEqual(sort_third([5, 6, 3, 4, 8, 9, 2]), [2, 6, 3, 4, 8, 9, 5])
        self.assertEqual(sort_third([1, 3, 2, 4, 5, 6, 7, 9, 8]), [2, 3, 1, 4, 5, 6, 9, 7, 8])
        self.assertEqual(sort_third([1, 2]), [1, 2])
        self.assertEqual(sort_third([1]), [1])
        self.assertEqual(sort_third([]), [])

if __name__ == '__main__':
    unittest.main()