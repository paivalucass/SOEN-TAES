def is_Sub_Array(A, B):
    if not A or not B:
        raise ValueError("Input lists cannot be empty")
    
    if len(A) > len(B):
        return False
    
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