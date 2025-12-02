def encrypt(s):
    encrypted_string = ''
    for char in s:
        if char.isalpha():
            shift = ((ord(char) - 97 + 2) * 2) % 26
            if char.islower():
                encrypted_char = chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
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