import re

def remove_lowercase(str1):
    result = re.sub(r'[a-z]', '', str1)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_lowercase('PYTHon'), 'PYTH')

if __name__ == '__main__':
    unittest.main()