def is_Sub_Array(A, B):
    if not all(isinstance(i, int) for i in A) or not all(isinstance(i, int) for i in B):
        raise TypeError("Input lists should only contain integers")
    for i in range(len(A) - len(B) + 1):
        if B == A[i:i + len(B)]:
            return True
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Sub_Array([1,4,3,5],[1,2]), False)

if __name__ == '__main__':
    unittest.main()