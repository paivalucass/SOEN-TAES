def next_smallest_palindrome(num):
    def is_palindrome(n):
        return str(n) == str(n)[::-1]
    
    if type(num) != int:
        return "Error"
    if num < 0:
        return 0
    
    num += 1
    while not is_palindrome(num):
        num += 1
    return num
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(next_smallest_palindrome(99), 101)

if __name__ == '__main__':
    unittest.main()