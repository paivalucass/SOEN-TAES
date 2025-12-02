def even_odd_palindrome(n):
    even_count = 0
    odd_count = 0
    for num in range(1, n+1):
        if num % 2 == 0 and str(num) == str(num)[::-1]:
            even_count += 1
        elif num % 2 != 0 and str(num) == str(num)[::-1]:
            odd_count += 1
    return (even_count, odd_count)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_odd_palindrome(3), (1, 2))

if __name__ == '__main__':
    unittest.main()