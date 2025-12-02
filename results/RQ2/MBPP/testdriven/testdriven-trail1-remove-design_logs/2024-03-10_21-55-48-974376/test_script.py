def is_octagonal(n):
    '''Write a function to find the nth octagonal number.'''
    return n * (3 * n - 2)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_octagonal(5), 65)

if __name__ == '__main__':
    unittest.main()