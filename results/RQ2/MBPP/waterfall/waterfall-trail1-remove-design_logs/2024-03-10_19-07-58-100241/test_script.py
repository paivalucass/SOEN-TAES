def pancake_sort(nums):
    if len(nums) <= 1:
        return nums
    
    def flip(arr, k):
        i = 0
        while i < k // 2:
            arr[i], arr[k-i-1] = arr[k-i-1], arr[i]
            i += 1
    
    def find_max_index(arr, k):
        max_index = 0
        for i in range(1, k):
            if arr[i] > arr[max_index]:
                max_index = i
        return max_index
    
    n = len(nums)
    for i in range(n-1, 0, -1):
        max_index = find_max_index(nums, i+1)
        if max_index != i:
            flip(nums, max_index+1)
            flip(nums, i+1)
    
    return nums
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(pancake_sort([15, 79, 25, 38, 69]), [15, 25, 38, 69, 79])

if __name__ == '__main__':
    unittest.main()