def find_star_num(n):
    '''Write a function to find the n'th star number.'''
    return (6 * n * (n - 1)) + 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_star_num(3), 37)

if __name__ == '__main__':
    unittest.main()