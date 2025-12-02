def is_decimal(num_str):
    try:
        num = round(float(num_str), 2)
        return True
    except ValueError:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_decimal('123.11'), True)

if __name__ == '__main__':
    unittest.main()