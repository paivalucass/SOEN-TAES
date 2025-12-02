def comb_sort(nums):
    # Implementing the comb sort algorithm
    def getNextGap(gap):
        # Shrink gap by Shrink factor
        gap = (gap * 10) / 13
        if gap < 1:
            return 1
        return int(gap)

    # Initialize gap
    n = len(nums)
    gap = n

    # Initialize swapped as true to make sure that the loop runs
    swapped = True

    # Keep running while gap is more than 1 and last iteration caused a swap
    while gap != 1 or swapped == True:
        # Find next gap
        gap = getNextGap(gap)

        # Initialize swapped as false so that we can check if a swap occurred in this iteration
        swapped = False

        # Compare all elements with current gap
        for i in range(0, n - gap):
            if nums[i] > nums[i + gap]:
                # Swap elements
                nums[i], nums[i + gap] = nums[i + gap], nums[i]
                # Set swapped to true to indicate a swap occurred
                swapped = True

    return nums

# Test the function with the provided assertion
assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
import unittest

class Test(unittest.TestCase):
    def test_comb_sort(self):
        self.assertEqual(comb_sort([5, 15, 37, 25, 79]), [5, 15, 25, 37, 79])

if __name__ == '__main__':
    unittest.main()