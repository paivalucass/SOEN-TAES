def even_odd_palindrome(n):
    even_count = 0
    odd_count = 0
    for num in range(1, n+1):
        if str(num) == str(num)[::-1]:
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    return (even_count, odd_count)
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(even_odd_palindrome(3), (1, 2))

    def test2(self):
        self.assertEqual(even_odd_palindrome(12), (4, 6))

if __name__ == '__main__':
    unittest.main()