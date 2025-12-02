import re

def number_ctr(input_str):
    digits = re.findall(r'\d', input_str)
    return len(digits)
import unittest

class Test(unittest.TestCase):
    def test_number_ctr(self):
        self.assertEqual(number_ctr('program2bedone'), 1)

if __name__ == '__main__':
    unittest.main()