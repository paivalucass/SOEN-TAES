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
    # Input validation to ensure 'a' is an integer
    if not isinstance(a, int):
        return False
    # Optimization to check if 'a' is a cube of some integer number
    if a < 0:
        return a == -round((-a)**(1/3))**3
    else:
        return a == round(a**(1/3))**3
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