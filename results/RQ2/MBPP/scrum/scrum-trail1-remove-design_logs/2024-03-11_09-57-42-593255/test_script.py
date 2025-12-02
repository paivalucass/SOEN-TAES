def is_Monotonic(A):
    increasing = True
    decreasing = True
    
    for i in range(1, len(A)):
        if A[i] > A[i-1]:
            decreasing = False
        elif A[i] < A[i-1]:
            increasing = False
    
    return increasing or decreasing
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Monotonic([6, 5, 4, 4]), True)

if __name__ == '__main__':
    unittest.main()