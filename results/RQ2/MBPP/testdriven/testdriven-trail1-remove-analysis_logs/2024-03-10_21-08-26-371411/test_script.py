def is_Monotonic(A):
    '''Write a python function to check whether the given array is monotonic or not.'''
    
    is_increasing = True
    is_decreasing = True
    
    if len(A) <= 1:
        return True
    
    for i in range(len(A)-1):
        if A[i] < A[i+1]:
            is_decreasing = False
        elif A[i] > A[i+1]:
            is_increasing = False
    
    return is_increasing or is_decreasing
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Monotonic([6, 5, 4, 4]), True)

if __name__ == '__main__':
    unittest.main()