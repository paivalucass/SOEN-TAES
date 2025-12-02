def check_min_heap_helper(arr, i):
    '''Write a function to check if the given array represents min heap or not. https://www.geeksforgeeks.org/how-to-check-if-a-given-array-represents-a-binary-heap/
    assert check_min_heap([1, 2, 3, 4, 5, 6]) == True'''
    if not arr:
        raise ValueError("Input array is empty")
    n = len(arr)
    for i in range((n // 2) - 1, -1, -1):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] > arr[left]:
            return False
        if right < n and arr[i] > arr[right]:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_min_heap_helper([1, 2, 3, 4, 5, 6], 0), True)

if __name__ == '__main__':
    unittest.main()