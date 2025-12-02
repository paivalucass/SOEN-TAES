def max_sub_array_sum_repeated(a, n, k):
    # Repeat the given array k times to form the modified array
    modified_arr = a * k
    
    # Find the largest sum of a contiguous array in the modified array using Kadane's algorithm
    max_sum = max_end = modified_arr[0]
    for i in range(1, len(modified_arr)):
        max_end = max(modified_arr[i], max_end + modified_arr[i])
        max_sum = max(max_sum, max_end)
    
    return max_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3), 30)

if __name__ == '__main__':
    unittest.main()