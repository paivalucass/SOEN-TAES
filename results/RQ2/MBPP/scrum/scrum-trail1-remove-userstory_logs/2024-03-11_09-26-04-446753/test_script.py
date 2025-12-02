def is_decimal(num):
    num = num.strip()
    if num[0] in ['+', '-']:
        num = num[1:]
    if '.' in num:
        integer_part, decimal_part = num.split('.')
        if len(decimal_part) <= 2 and decimal_part.isdigit():
            return True
    elif num.isdigit():
        return True
    return False

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_decimal('123.11'), True)

if __name__ == '__main__':
    unittest.main()