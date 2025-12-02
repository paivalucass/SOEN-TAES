def is_Sub_Array(A, B):
    for i in range(len(A) - len(B) + 1):
        if A[i:i + len(B)] == B:
            return True
    return False

# Test Cases:

# Test Title: Verify if B is a sublist of A
# Input Data: A=[1, 2, 3, 4, 5], B=[2, 3, 4]
# Expected Output: True

# Test Title: Verify if B is not a sublist of A
# Input Data: A=[1, 4, 3, 5], B=[1, 2]
# Expected Output: False

# Test Title: Verify if B is an empty sublist of A
# Input Data: A=[1, 2, 3, 4, 5], B=[]
# Expected Output: True

# Test Title: Verify if B is not a sublist of A with negative numbers
# Input Data: A=[1, 2, 3, 4, 5], B=[-2, -3, -4]
# Expected Output: False

# Test Title: Verify if B is a sublist of A with repeated numbers
# Input Data: A=[1, 2, 2, 3, 4, 5], B=[2, 2, 3]
# Expected Output: True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Sub_Array([1,4,3,5],[1,2]), False)

if __name__ == '__main__':
    unittest.main()