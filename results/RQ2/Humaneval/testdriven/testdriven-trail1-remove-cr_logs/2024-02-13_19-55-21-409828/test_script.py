def encrypt(s):
    encrypted_string = ""
    for char in s:
        if char.isalpha():
            shift = 2
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
            encrypted_char = chr(((ord(char) - base + shift) * 2) % 26 + base)
            encrypted_string += encrypted_char
        else:
            encrypted_string += char
    return encrypted_string
import unittest

class Test(unittest.TestCase):
    def test_encrypt(self):
        self.assertEqual(encrypt('hi'), 'lm')
        self.assertEqual(encrypt('asdfghjkl'), 'ewhjklnop')
        self.assertEqual(encrypt('gf'), 'kj')
        self.assertEqual(encrypt('et'), 'ix')

if __name__ == '__main__':
    unittest.main()