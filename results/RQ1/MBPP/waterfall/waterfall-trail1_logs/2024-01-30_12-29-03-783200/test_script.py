def next_smallest_palindrome(num):
    """
    This function takes a number and returns the next smallest palindrome number.
    """
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