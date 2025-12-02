def get_Char(strr):
    total = 0
    for ch in strr:
        total += ord(ch) - 97
    result = chr((total % 26) + 97)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_Char('abc'), 'f')

if __name__ == '__main__':
    unittest.main()