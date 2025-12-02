def is_Sub_Array(A, B):
    def check_input_lists(A, B):
        if not A or not B:
            raise ValueError("Input lists cannot be empty")
        if any(type(item) != type(A[0]) for item in A) or any(type(item) != type(B[0]) for item in B):
            raise TypeError("Input lists should contain elements of the same type")

    check_input_lists(A, B)
    
    return all(item in B for item in A)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Sub_Array([1,4,3,5],[1,2]), False)

if __name__ == '__main__':
    unittest.main()