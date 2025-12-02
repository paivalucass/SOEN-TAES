def sort_third(l: list):
    result = l.copy()
    to_sort = {}
    for i in range(len(l)):
        if i % 3 == 0:
            to_sort[i] = l[i]
    sorted_values = sorted(to_sort.values())
    for i in range(len(result)):
        if i % 3 == 0:
            result[i] = sorted_values.pop(0)
    return result
import unittest

class Test(unittest.TestCase):
    def test_sort_third(self):
        self.assertEqual(sort_third([1, 2, 3]), [1, 2, 3])
        self.assertEqual(sort_third([5, 6, 3, 4, 8, 9, 2]), [2, 6, 3, 4, 8, 9, 5])

if __name__ == '__main__':
    unittest.main()