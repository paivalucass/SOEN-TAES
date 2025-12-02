def is_Monotonic(A):
    # Check if the array is strictly increasing
    if all(A[i] <= A[i+1] for i in range(len(A) - 1)):
        return True
    # Check if the array is strictly decreasing
    elif all(A[i] >= A[i+1] for i in range(len(A) - 1)):
        return True
    # If neither strictly increasing nor strictly decreasing, the array is not monotonic
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Monotonic([6, 5, 4, 4]), True)

if __name__ == '__main__':
    unittest.main()