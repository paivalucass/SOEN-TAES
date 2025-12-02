def sort_even(l: list):
    even_indices = [i for i in range(len(l)) if i % 2 == 0]
    even_values = [l[i] for i in even_indices]
    even_values.sort()
    for i in even_indices:
        l[i] = even_values.pop(0)
    return l
import unittest

class Test(unittest.TestCase):
    def test_sort_even(self):
        self.assertEqual(sort_even([1, 2, 3]), [1, 2, 3])
        self.assertEqual(sort_even([5, 6, 3, 4]), [3, 6, 5, 4])

if __name__ == '__main__':
    unittest.main()