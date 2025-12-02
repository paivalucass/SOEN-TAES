def left_insertion(arr, x):
    if len(arr) == 0:
        return 0
    
    if x < arr[0]:
        return 0
    
    if x > arr[-1]:
        return len(arr)
    
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    
    return left
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(left_insertion([1,2,4,5], 6), 4)

if __name__ == '__main__':
    unittest.main()