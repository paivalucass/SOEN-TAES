def is_cube_number(a):
    '''
    Write a function that takes an integer a and returns True 
    if this integer is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    is_cube_number(1) ==> True
    is_cube_number(2) ==> False
    is_cube_number(-1) ==> True
    is_cube_number(64) ==> True
    is_cube_number(0) ==> True
    is_cube_number(180) ==> False
    '''
    if a >= 0:
        cube_root = round(a ** (1/3))
        return cube_root ** 3 == a
    else:
        return False

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