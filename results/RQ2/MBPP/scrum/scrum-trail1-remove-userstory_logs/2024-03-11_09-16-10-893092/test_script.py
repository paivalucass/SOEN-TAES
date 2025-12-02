def is_Sub_Array(A, B):
    if not B:
        return True
    if not A or len(A) < len(B):
        return False
    for i in range(len(A)):
        if A[i] == B[0]:
            if A[i:i + len(B)] == B:
                return True
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Sub_Array([1,4,3,5],[1,2]), False)

if __name__ == '__main__':
    unittest.main()