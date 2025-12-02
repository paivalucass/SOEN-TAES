def is_upper(string):
    return string.upper()
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_upper('person'), 'PERSON')

if __name__ == '__main__':
    unittest.main()