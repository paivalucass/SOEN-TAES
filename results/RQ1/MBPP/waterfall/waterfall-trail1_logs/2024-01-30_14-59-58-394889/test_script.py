def find_first_occurrence(A, x):
    if not A or not all(isinstance(i, (int, float)) for i in A) or not isinstance(x, (int, float)):
        return -1
    
    if A != sorted(A):
        return -1
    
    left = 0
    right = len(A) - 1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == x:
            while mid > 0 and A[mid - 1] == x:
                mid -= 1
            return mid
        elif A[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5), 1)

if __name__ == '__main__':
    unittest.main()