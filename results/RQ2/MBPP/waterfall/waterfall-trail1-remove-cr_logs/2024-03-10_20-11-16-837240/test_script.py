def find_kth(arr1, arr2, k):
    combined_array = arr1 + arr2
    combined_array.sort()
    if len(combined_array) < k:
        return "None"
    elif not all(isinstance(x, int) for x in combined_array):
        return "Invalid Input"
    else:
        return combined_array[k - 1]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5), 6)

if __name__ == '__main__':
    unittest.main()