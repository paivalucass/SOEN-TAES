def is_Sub_Array(A, B):
    '''Write a python function to check whether a list is sublist of another or not.'''
    if not isinstance(A, list) or not isinstance(B, list):
        return False
    
    if len(B) == 0:
        return False

    for i in range(len(A) - len(B) + 1):
        if A[i:i+len(B)] == B:
            return True
    
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Sub_Array([1,4,3,5],[1,2]), False)

if __name__ == '__main__':
    unittest.main()