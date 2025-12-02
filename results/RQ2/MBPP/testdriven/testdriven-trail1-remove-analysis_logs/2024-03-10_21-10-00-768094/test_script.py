def next_smallest_palindrome(num):
    '''
    Write a function to find the next smallest palindrome of a specified integer, returned as an integer.
    assert next_smallest_palindrome(99)==101
    '''

    if not isinstance(num, int):
        raise ValueError("Input must be an integer")
    if num < 0:
        raise ValueError("Input must be a positive integer")

    def is_palindrome(s):
        return s == s[::-1]

    num += 1
    while True:
        if is_palindrome(str(num)):
            return num
        num += 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(next_smallest_palindrome(99), 101)

if __name__ == '__main__':
    unittest.main()