def dif_Square(n):
    '''Write a python function to check whether the given number can be represented as the difference of two squares or not.'''
    if n < 0 or n % 2 != 0:
        return True
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dif_Square(5), True)

if __name__ == '__main__':
    unittest.main()