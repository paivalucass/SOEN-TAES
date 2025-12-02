def is_decimal(num: str) -> bool:
    import re

    decimal_pattern = r'^\s*-?\d+\.\d{2}\s*$'

    if isinstance(num, str):
        if re.match(decimal_pattern, num.strip()):
            return True
        else:
            return False
    else:
        raise ValueError("Input must be a string")
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_decimal('123.11'), True)

if __name__ == '__main__':
    unittest.main()