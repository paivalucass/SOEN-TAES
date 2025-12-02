def is_upper(string):
    if string is None:
        return "ERROR: NULL INPUT"
    elif not isinstance(string, str):
        return "ERROR: INVALID INPUT"
    else:
        return string.upper()
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_upper('person'), 'PERSON')

if __name__ == '__main__':
    unittest.main()