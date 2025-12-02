def hex_key(num):
    prime_hex_digits = ["2", "3", "5", "7", "B", "D"]
    count = 0
    for digit in num:
        if digit in prime_hex_digits:
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test('AB'), 1)
        self.assertEqual(function_under_test('1077E'), 2)
        self.assertEqual(function_under_test('ABED1A33'), 4)
        self.assertEqual(function_under_test('123456789ABCDEF0'), 6)
        self.assertEqual(function_under_test('2020'), 2)

if __name__ == '__main__':
    unittest.main()