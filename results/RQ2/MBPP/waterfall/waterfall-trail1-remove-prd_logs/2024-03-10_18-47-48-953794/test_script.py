def is_decimal(num):
    import re
    if num is None:
        return False
    num = num.strip()
    if not num:
        return False

    pattern = re.compile(r'^-?\d+\.\d{1,2}$')
    if not pattern.match(num):
        return False

    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_decimal('123.11'), True)

if __name__ == '__main__':
    unittest.main()