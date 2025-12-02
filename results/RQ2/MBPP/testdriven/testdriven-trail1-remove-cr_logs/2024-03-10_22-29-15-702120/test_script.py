def get_Char(strr):
    total_ascii = 0
    for char in strr:
        total_ascii += ord(char)
    result = chr(((total_ascii - len(strr)*97) % 26) + 97)
    return result

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_Char('abc'), 'f')

if __name__ == '__main__':
    unittest.main()