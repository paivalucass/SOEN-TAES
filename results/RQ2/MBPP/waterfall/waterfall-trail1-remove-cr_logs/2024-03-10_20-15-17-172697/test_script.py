def find_first_occurrence(A, x):
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
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5), 1)

if __name__ == '__main__':
    unittest.main()