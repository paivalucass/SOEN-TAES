def sort_third(l: list) -> list:
    try:
        if not l or not all(isinstance(x, int) for x in l):
            raise ValueError("Input list must not be empty and must contain only integers.")
        
        third_indices = [i for i in range(len(l)) if i % 3 == 0]
        third_elements = [l[i] for i in third_indices]
        sorted_third_elements = sorted(third_elements)
        
        for i, val in zip(third_indices, sorted_third_elements):
            l[i] = val
        
        return l
        
    except ValueError as e:
        return str(e)
import unittest

class Test(unittest.TestCase):
    def test_sort_third(self):
        self.assertEqual(sort_third([1, 2, 3]), [1, 2, 3])
        self.assertEqual(sort_third([5, 6, 3, 4, 8, 9, 2]), [2, 6, 3, 4, 8, 9, 5])

if __name__ == '__main__':
    unittest.main()