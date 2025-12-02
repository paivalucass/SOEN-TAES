def hex_key(num):
    PRIME_DIGITS = '2357BD'
    count = 0
    for digit in num:
        if digit in PRIME_DIGITS:
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(hex_key("AB"), 1)

    def test2(self):
        self.assertEqual(hex_key("1077E"), 2)

    def test3(self):
        self.assertEqual(hex_key("ABED1A33"), 4)

    def test4(self):
        self.assertEqual(hex_key("123456789ABCDEF0"), 6)

    def test5(self):
        self.assertEqual(hex_key("2020"), 2)

if __name__ == '__main__':
    unittest.main()