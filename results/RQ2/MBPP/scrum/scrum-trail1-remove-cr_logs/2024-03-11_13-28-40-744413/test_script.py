def remove_lowercase(str1):
    import re
    return re.sub(r'[a-z]', '', str1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_lowercase('PYTHon'), 'PYTH')

if __name__ == '__main__':
    unittest.main()