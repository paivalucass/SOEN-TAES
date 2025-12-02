def next_smallest_palindrome(num):
    num += 1
    while True:
        if str(num) == str(num)[::-1]:
            return num
        num += 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(next_smallest_palindrome(99), 101)

if __name__ == '__main__':
    unittest.main()