def find_kth(arr1, arr2, k):
    if not isinstance(arr1, list) or not isinstance(arr2, list) or not isinstance(k, int) or k <= 0:
        return "Invalid Input"
    
    merged_array = sorted(arr1 + arr2)
    if k > len(merged_array):
        return "Invalid Input"
    
    return merged_array[k-1]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5), 6)

if __name__ == '__main__':
    unittest.main()