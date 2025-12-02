def is_Monotonic(A):
    if len(A) <= 1:
        return True
    increasing = all(A[i] <= A[i+1] for i in range(len(A)-1))
    decreasing = all(A[i] >= A[i+1] for i in range(len(A)-1))
    return increasing or decreasing
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Monotonic([6, 5, 4, 4]), True)

if __name__ == '__main__':
    unittest.main()