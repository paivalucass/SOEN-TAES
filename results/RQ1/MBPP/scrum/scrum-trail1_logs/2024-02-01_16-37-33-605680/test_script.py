def find_first_occurrence(A, x):
    '''
    Function to find the index of the first occurrence of a given number in a sorted array.

    :param A: Sorted array
    :param x: Number to find
    :return: Index of the first occurrence of the given number in the input array, -1 if not found
    '''
    left = 0
    right = len(A) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if A[mid] == x:
            result = mid
            right = mid - 1
        elif A[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return result

assert find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5) == 1
assert find_first_occurrence([1,2,3,4,5], 3) == 2
assert find_first_occurrence([1,1,2,2,3,3], 2) == 2
assert find_first_occurrence([1,2,3,4,5], 6) == -1
assert find_first_occurrence([2,5,5,5,6,6,8,9,9,9], 5) == 1
assert find_first_occurrence([2,5,5,5,6,6,8,9,9,9], 2) == 0
assert find_first_occurrence([2,5,5,5,6,6,8,9,9,9], 7) == -1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5), 1)

if __name__ == '__main__':
    unittest.main()