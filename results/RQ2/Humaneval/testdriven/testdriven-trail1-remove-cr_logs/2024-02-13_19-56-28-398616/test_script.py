def encrypt(s):
    result = ""
    for char in s:
        if char.isalpha():
            shift = (ord(char) - 97 + 2 * 2) % 26
            result += chr(shift + 97) if shift != 0 else 'z'
        else:
            result += char
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(encrypt('hi'), 'lm')
        self.assertEqual(encrypt('asdfghjkl'), 'ewhjklnop')
        self.assertEqual(encrypt('gf'), 'kj')
        self.assertEqual(encrypt('et'), 'ix')

if __name__ == '__main__':
    unittest.main()