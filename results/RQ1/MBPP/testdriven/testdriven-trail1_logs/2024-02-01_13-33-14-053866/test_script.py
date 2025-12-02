def is_perfect_square(n) :
    '''Write a function to check whether the given number is a perfect square or not.'''
    return n**0.5 == int(n**0.5)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(is_perfect_square(9))
        self.assertFalse(is_perfect_square(10))

if __name__ == '__main__':
    unittest.main()