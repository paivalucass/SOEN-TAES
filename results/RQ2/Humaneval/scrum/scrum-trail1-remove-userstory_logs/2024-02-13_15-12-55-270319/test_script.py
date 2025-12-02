def hex_key(hex_num):
    prime_hex_digits = {'2', '3', '5', '7', 'B', 'D'}
    count = 0
    
    for digit in hex_num:
        if digit.upper() in prime_hex_digits:
            count += 1
    
    return count
import unittest

class Test(unittest.TestCase):
    def test_hex_key(self):
        self.assertEqual(hex_key('AB'), 1)
        self.assertEqual(hex_key('1077E'), 2)
        self.assertEqual(hex_key('ABED1A33'), 4)
        self.assertEqual(hex_key('123456789ABCDEF0'), 6)
        self.assertEqual(hex_key('2020'), 2)

if __name__ == '__main__':
    unittest.main()