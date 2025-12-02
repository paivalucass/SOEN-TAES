def is_Sub_Array(A, B):
    '''
    Write a python function to check whether a list is a sublist of another or not.
    assert is_Sub_Array([1,4,3,5],[1,2]) == False
    '''

    if not isinstance(A, list) or not isinstance(B, list):
        return "Invalid Input"

    for item in A:
        if item not in B:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Sub_Array([1,4,3,5],[1,2]), False)

if __name__ == '__main__':
    unittest.main()