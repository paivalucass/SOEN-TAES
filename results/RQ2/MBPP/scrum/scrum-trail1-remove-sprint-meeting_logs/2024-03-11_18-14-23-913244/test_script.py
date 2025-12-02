def is_Monotonic(A):
    def input_validation(A):
        if len(A) == 0:
            return False
        if all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or all(A[i] >= A[i + 1] for i in range(len(A) - 1)):
            return True
        return False
    
    return input_validation(A)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Monotonic([6, 5, 4, 4]), True)

if __name__ == '__main__':
    unittest.main()