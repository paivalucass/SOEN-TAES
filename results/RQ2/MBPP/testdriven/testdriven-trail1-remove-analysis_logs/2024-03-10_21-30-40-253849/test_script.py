def last(arr, x):
    '''Write a python function to find the last position of an element in a sorted array.'''
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < x:
            start = mid + 1
        elif arr[mid] > x:
            end = mid - 1
        else:  # arr[mid] == x
            if mid == len(arr)-1 or arr[mid+1] != x:
                return mid
            else:
                start = mid + 1
    return -1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(last([1, 2, 3], 1), 0)

if __name__ == '__main__':
    unittest.main()