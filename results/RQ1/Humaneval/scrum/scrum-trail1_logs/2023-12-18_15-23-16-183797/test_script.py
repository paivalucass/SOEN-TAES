def validate_hexadecimal_input(num):
    if num == "":
        return False
    if all(c in "0123456789ABCDEF" for c in num):
        return True
    else:
        return False

def count_prime_hex_digits(num):
    prime_count = 0
    for digit in num:
        if digit in "2357BD":
            prime_count += 1
    return prime_count

def hex_key(num):
    if not validate_hexadecimal_input(num):
        return 0
    return count_prime_hex_digits(num)
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