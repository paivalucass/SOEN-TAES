def sort_even(l: list):
    if len(l) == 0:
        return []
    
    even_indices = [i for i in range(0, len(l), 2)]
    even_values = [l[i] for i in even_indices]
    sorted_even_values = sorted(even_values)
    
    result = l.copy()
    
    for i, val in zip(even_indices, sorted_even_values):
        result[i] = val
    
    return result
import unittest

class Test(unittest.TestCase):
    def test_sort_even(self):
        self.assertEqual(sort_even([1, 2, 3]), [1, 2, 3])
        self.assertEqual(sort_even([5, 6, 3, 4]), [3, 6, 5, 4])

if __name__ == '__main__':
    unittest.main()