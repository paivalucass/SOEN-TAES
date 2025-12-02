def is_decimal(num: str) -> bool:
    import re
    decimal_pattern = re.compile(r'^\d+\.\d{2}$')
    return bool(decimal_pattern.match(num))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_decimal('123.11'), True)

if __name__ == '__main__':
    unittest.main()