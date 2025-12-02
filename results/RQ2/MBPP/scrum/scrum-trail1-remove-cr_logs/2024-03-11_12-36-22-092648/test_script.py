def get_Char(strr):
    total_ascii = sum(ord(char) for char in strr)
    return chr(97 + ((total_ascii - len(strr)*97) % 26))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_Char('abc'), 'f')

if __name__ == '__main__':
    unittest.main()