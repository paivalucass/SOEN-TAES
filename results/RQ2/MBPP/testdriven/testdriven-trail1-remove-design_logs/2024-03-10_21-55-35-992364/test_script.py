def is_woodall(x):
    '''Write a function to check if the given number is Woodall or not.'''
    if x <= 0:
        return False
    else:
        n = 1
        while n * (2**n - 1) <= x:
            if n * (2**n - 1) == x:
                return True
            n += 1
        return False
import unittest

class Test(unittest.TestCase):
    def test_woodall_number(self):
        self.assertTrue(is_woodall(383))

if __name__ == '__main__':
    unittest.main()