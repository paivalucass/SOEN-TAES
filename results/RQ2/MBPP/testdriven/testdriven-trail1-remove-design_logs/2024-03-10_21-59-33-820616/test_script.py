def pancake_sort(nums):
    def flip(arr, k):
        i = 0
        while i < k / 2:
            temp = arr[i]
            arr[i] = arr[k - i - 1]
            arr[k - i - 1] = temp
            i += 1

    for k in range(len(nums), 0, -1):
        max_index = nums.index(max(nums[:k]))
        if max_index != k - 1:
            flip(nums, max_index + 1)
            flip(nums, k)

    return nums

# Test cases
assert pancake_sort([]) == []
assert pancake_sort([7]) == [7]
assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(pancake_sort([15, 79, 25, 38, 69]), [15, 25, 38, 69, 79])

if __name__ == '__main__':
    unittest.main()