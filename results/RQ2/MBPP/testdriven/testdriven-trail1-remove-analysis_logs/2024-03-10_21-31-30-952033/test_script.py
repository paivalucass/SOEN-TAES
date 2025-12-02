def is_woodall(x):
    '''Function to check if the given number is a Woodall number or not.'''
    if x <= 0:
        return False
    if x == 1:
        return False
    n = 1
    while True:
        woodall_number = n * 2**n - 1
        if woodall_number == x:
            return True
        if woodall_number > x:
            return False
        n += 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_woodall(383), True)

if __name__ == '__main__':
    unittest.main()