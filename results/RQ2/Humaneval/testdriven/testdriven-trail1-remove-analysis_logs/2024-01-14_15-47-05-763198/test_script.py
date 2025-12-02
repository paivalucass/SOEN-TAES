def sort_even(l: list):
    even_indices = [l[i] for i in range(len(l)) if i % 2 == 0]
    even_indices.sort()
    
    result = [even_indices.pop(0) if i % 2 == 0 else l[i] for i in range(len(l))]
    
    return result
import unittest

class Test(unittest.TestCase):
    def test_sort_even(self):
        self.assertEqual(sort_even([1, 2, 3]), [1, 2, 3])
        self.assertEqual(sort_even([5, 6, 3, 4]), [3, 6, 5, 4])

if __name__ == '__main__':
    unittest.main()