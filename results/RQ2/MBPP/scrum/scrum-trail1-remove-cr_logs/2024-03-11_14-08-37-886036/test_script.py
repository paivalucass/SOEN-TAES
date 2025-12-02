def get_Char(strr):
    total = 0
    for char in strr:
        total += ord(char)
    return chr((total % 26) + 97)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_Char('abc'), 'f')

if __name__ == '__main__':
    unittest.main()