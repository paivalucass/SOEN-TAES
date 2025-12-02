def pancake_sort(nums):
    # Function to flip the subarray from index 0 to k
    def flip(arr, k):
        return arr[:k+1][::-1] + arr[k+1:]

    # Function to find the index of the maximum element in the subarray from 0 to end
    def find_max_index(arr, end):
        max_index = 0
        for i in range(end+1):
            if arr[i] > arr[max_index]:
                max_index = i
        return max_index

    # Main pancake sort logic
    for end in range(len(nums)-1, 0, -1):
        max_index = find_max_index(nums, end)
        if max_index != end:
            nums = flip(nums, max_index)
            nums = flip(nums, end)
    return nums

# Test the pancake_sort function
assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(pancake_sort([15, 79, 25, 38, 69]), [15, 25, 38, 69, 79])

if __name__ == '__main__':
    unittest.main()