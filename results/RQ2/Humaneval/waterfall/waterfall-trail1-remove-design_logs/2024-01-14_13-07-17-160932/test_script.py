def sort_third(l: list):
    result = l.copy()
    indices_divisible_by_three = [i for i in range(len(l)) if i % 3 == 0]
    values_divisible_by_three = [l[i] for i in indices_divisible_by_three]
    values_divisible_by_three.sort()  # Sort the values in place
    for i, v in zip(indices_divisible_by_three, values_divisible_by_three):
        result[i] = v
    return result
import unittest

class Test(unittest.TestCase):
    def test_sort_third(self):
        self.assertEqual(sort_third([1, 2, 3]), [1, 2, 3])
        self.assertEqual(sort_third([5, 6, 3, 4, 8, 9, 2]), [2, 6, 3, 4, 8, 9, 5])

if __name__ == '__main__':
    unittest.main()