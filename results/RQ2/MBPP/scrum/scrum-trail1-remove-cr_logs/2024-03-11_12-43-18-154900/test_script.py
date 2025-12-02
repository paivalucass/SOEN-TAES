def search(arr):
    left = 0
    right = len(arr) - 1
    
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return arr[0]
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] != arr[mid-1] and arr[mid] != arr[mid+1]:
            return arr[mid]
        elif (mid % 2 == 0 and arr[mid] == arr[mid+1]) or (mid % 2 != 0 and arr[mid] == arr[mid-1]):
            left = mid + 1
        else:
            right = mid - 1

    return arr[left]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(search([1,1,2,2,3]), 3)

if __name__ == '__main__':
    unittest.main()