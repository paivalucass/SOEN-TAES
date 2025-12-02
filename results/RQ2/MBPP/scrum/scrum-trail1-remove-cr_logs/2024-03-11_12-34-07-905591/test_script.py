def is_Monotonic(A):
    increasing = True
    decreasing = True

    for i in range(len(A) - 1):
        if A[i] > A[i+1]:
            increasing = False
        elif A[i] < A[i+1]:
            decreasing = False

    return increasing or decreasing
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Monotonic([6, 5, 4, 4]), True)

if __name__ == '__main__':
    unittest.main()