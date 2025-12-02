def find_first_occurrence(A, x):
    '''Write a function to find the index of the first occurrence of a given number in a sorted array.'''
    start = 0  # Initialize start index
    end = len(A) - 1  # Initialize end index
    result = -1  # Initialize result index
    while start <= end:  # Loop until start index is less than or equal to end index
        mid = (start + end) // 2  # Calculate the middle index
        if A[mid] == x:  # If the middle element is equal to the given number
            result = mid  # Update result index to the middle index
            end = mid - 1  # Move end index to the left of the middle index
        elif A[mid] < x:  # If the middle element is less than the given number
            start = mid + 1  # Move start index to the right of the middle index
        else:  # If the middle element is greater than the given number
            end = mid - 1  # Move end index to the left of the middle index
    return result  # Return the index of the first occurrence of the given number

assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1  # Test case to find the first occurrence of 5 in the array

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5), 1)

if __name__ == '__main__':
    unittest.main()