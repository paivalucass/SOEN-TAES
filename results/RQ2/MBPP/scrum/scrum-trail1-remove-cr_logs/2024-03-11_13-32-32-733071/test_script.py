def is_Sub_Array(A, B):
    if not A:
        return True
    if not B or len(B) < len(A):
        return False
    
    # Use sliding window approach to check for subarray
    for i in range(len(B) - len(A) + 1):
        if B[i:i+len(A)] == A:
            return True
    
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Sub_Array([1,4,3,5],[1,2]), False)

if __name__ == '__main__':
    unittest.main()