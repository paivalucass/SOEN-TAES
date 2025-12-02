def find_first_occurrence(A, x):
    if len(A) == 0:
        return -1
    
    low = 0
    high = len(A) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if A[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    
    if low < len(A) and A[low] == x:
        return low
    else:
        return -1
import unittest

class Test(unittest.TestCase):
    def test_find_first_occurrence(self):
        self.assertEqual(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5), 1)

if __name__ == '__main__':
    unittest.main()