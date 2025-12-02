def find_first_occurrence(A, x):
    '''Write a function to find the index of the first occurrence of a given number in a sorted array.'''
    # Binary search algorithm to find the first occurrence of the target value
    low = 0
    high = len(A) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if A[mid] == x:
            result = mid
            high = mid - 1
        elif A[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return result

# Test case
assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5), 1)

if __name__ == '__main__':
    unittest.main()