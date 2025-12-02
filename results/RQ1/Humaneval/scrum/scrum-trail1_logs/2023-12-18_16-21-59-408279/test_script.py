def encrypt(s):
    encrypted = ''
    for char in s:
        if char.isalpha():
            shifted = chr(((ord(char) - 97 + 4) % 26) + 97)
            encrypted += shifted
        else:
            encrypted += char
    return encrypted
import unittest

class Test(unittest.TestCase):
    def test_encrypt(self):
        self.assertEqual(encrypt('hi'), 'lm')
        self.assertEqual(encrypt('asdfghjkl'), 'ewhjklnop')
        self.assertEqual(encrypt('gf'), 'kj')
        self.assertEqual(encrypt('et'), 'ix')

if __name__ == '__main__':
    unittest.main()