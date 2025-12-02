def next_smallest_palindrome(num):
    if len(str(num)) == 1:
        return num + 1
    elif num > 10**9:
        return "Error: Input number is too large"
    
    if not isinstance(num, int):
        return "Error: Input is not an integer"
    
    def is_palindrome(n):
        return str(n) == str(n)[::-1]
    
    while True:
        num += 1
        if is_palindrome(num):
            return num
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(next_smallest_palindrome(99), 101)

if __name__ == '__main__':
    unittest.main()