def next_smallest_palindrome(num):
    '''Write a function to find the next smallest palindrome of a specified integer, returned as an integer.'''
    num += 1
    while str(num) != str(num)[::-1]:
        num += 1
    return num
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(next_smallest_palindrome(99), 101)

if __name__ == '__main__':
    unittest.main()