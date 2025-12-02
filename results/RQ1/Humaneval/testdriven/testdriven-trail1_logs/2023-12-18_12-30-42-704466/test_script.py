def hex_key(num):
    prime_count = 0
    for digit in num:
        if digit in ['2', '3', '5', '7', 'B', 'D']:
            prime_count += 1
    return prime_count
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