def sort_even(l: list[int]) -> list[int]:
    if not all(isinstance(i, int) for i in l):
        raise TypeError("Input list must contain only integers")
    even_indices = sorted([l[i] for i in range(0,len(l),2)])
    result = [even_indices[i//2] if i%2==0 else l[i] for i in range(len(l))]
    return result
import unittest

class Test(unittest.TestCase):
    def test_sort_even(self):
        self.assertEqual(sort_even([1, 2, 3]), [1, 2, 3])
        self.assertEqual(sort_even([5, 6, 3, 4]), [3, 6, 5, 4])
        self.assertEqual(sort_even([9, 8, 7, 6, 5, 4]), [4, 8, 7, 6, 5, 9])
        self.assertEqual(sort_even([10, 20, 30, 40, 50]), [10, 50, 30, 40, 20])

if __name__ == '__main__':
    unittest.main()