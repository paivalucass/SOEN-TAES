def even_odd_palindrome(n):
    def is_palindrome(num):
        return str(num) == str(num)[::-1]

    if not isinstance(n, int) or n <= 0:
        return "Input must be a positive integer"

    even_count = 0
    odd_count = 0

    for i in range(1, n+1):
        if is_palindrome(i):
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    return (even_count, odd_count)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_odd_palindrome(3), (1, 2))
        self.assertEqual(even_odd_palindrome(12), (4, 6))

if __name__ == '__main__':
    unittest.main()