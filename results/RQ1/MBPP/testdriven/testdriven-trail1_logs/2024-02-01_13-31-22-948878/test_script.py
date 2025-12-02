def last(arr, x):
    '''
    Write a python function to find the last position of an element in a sorted array.
    assert last([1,2,3],1) == 0
    '''

    if len(arr) == 0:
        return "Error: Array is empty"

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return "Error: Array is not sorted in ascending order"

    if x not in arr:
        return "Error: Element not found in array"

    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            result = mid
            left = mid + 1
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return result
import unittest

class Test(unittest.TestCase):
    def test_last_position(self):
        self.assertEqual(last([1,2,3], 1), 0)

if __name__ == '__main__':
    unittest.main()