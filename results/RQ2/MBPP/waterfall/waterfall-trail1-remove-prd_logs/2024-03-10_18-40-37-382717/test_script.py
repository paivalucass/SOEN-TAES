def remove_lowercase(input_string):
    import re
    return re.sub('[a-z]', '', input_string)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_lowercase('PYTHon'), 'PYTH')

if __name__ == '__main__':
    unittest.main()