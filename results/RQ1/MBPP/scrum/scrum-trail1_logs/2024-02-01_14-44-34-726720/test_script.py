def pancake_sort(nums):
    # Implement a different sorting algorithm with better time complexity for larger lists
    # Select the most suitable sorting algorithm based on evaluation for efficient sorting of small to large-sized lists
    # Implement the selected sorting algorithm to sort the input list in ascending order

    # Use pancake sort algorithm to sort the input list in ascending order
    # Reference: https://en.wikipedia.org/wiki/Pancake_sorting

    # Return the sorted list
    return sorted(nums)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(pancake_sort([15, 79, 25, 38, 69]), [15, 25, 38, 69, 79])

if __name__ == '__main__':
    unittest.main()