def even_odd_palindrome(n):
    even_count = 0
    odd_count = 0
    
    for i in range(1, n+1):
        num_str = str(i)
        length = len(num_str)
        
        if num_str == num_str[::-1]:
            if length % 2 == 0:
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