def find_star_num(n): 
    '''Write a function to find the n'th star number.'''
    if n <= 0:
        return 'Error: Invalid Input'
    elif n == 1:
        return 6
    else:
        return 6 + (5 * (n-1)) + find_star_num(n - 1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_star_num(3), 37)

if __name__ == '__main__':
    unittest.main()