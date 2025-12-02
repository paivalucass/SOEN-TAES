def hex_key(num):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def count_prime_digits(num):
        prime_digits = ['2', '3', '5', '7', 'B', 'D']
        count = 0
        for digit in num:
            if digit in prime_digits:
                count += 1
        return count

    if not num:
        return 0
    
    return count_prime_digits(num)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(hex_key('AB'), 1)
        self.assertEqual(hex_key('1077E'), 2)
        self.assertEqual(hex_key('ABED1A33'), 4)
        self.assertEqual(hex_key('123456789ABCDEF0'), 6)
        self.assertEqual(hex_key('2020'), 2)

if __name__ == '__main__':
    unittest.main()