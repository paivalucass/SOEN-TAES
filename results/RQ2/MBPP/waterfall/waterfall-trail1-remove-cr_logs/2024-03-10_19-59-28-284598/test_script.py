def is_num_decagonal(n):
    '''Write a function to find the nth decagonal number.'''
    if not isinstance(n, int) or n <= 0:
        return "Invalid Input: Negative Number" if n <= 0 else "Invalid Input: Non-numeric Characters"
    else:
        return n * (10 * n - 7)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_num_decagonal(3), 27)

if __name__ == '__main__':
    unittest.main()