def is_Sub_Array(A, B):
    if not isinstance(A, list) or not isinstance(B, list):
        raise TypeError("Both inputs should be lists")
    if len(B) == 0:
        return True
    if len(A) == 0:
        return False
    
    for i in range(len(A)):
        if A[i] == B[0]:
            if A[i:i+len(B)] == B:
                return True
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Sub_Array([1,4,3,5],[1,2]), False)

if __name__ == '__main__':
    unittest.main()