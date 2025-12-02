def iscube(a):
    '''
    Write a function that takes an integer a and returns True
    if this integer is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    '''
    # Check if the input is negative and convert it to positive
    if a < 0:
        a = -a
    
    # Calculate the cube root of the absolute value of the input
    cube_root = int(round(a ** (1/3)))
    
    # Check if the cube of the cube root is equal to the original input
    return cube_root ** 3 == a
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(iscube(1), True)
        self.assertEqual(iscube(2), False)
        self.assertEqual(iscube(-1), True)
        self.assertEqual(iscube(64), True)
        self.assertEqual(iscube(0), True)
        self.assertEqual(iscube(180), False)

if __name__ == '__main__':
    unittest.main()