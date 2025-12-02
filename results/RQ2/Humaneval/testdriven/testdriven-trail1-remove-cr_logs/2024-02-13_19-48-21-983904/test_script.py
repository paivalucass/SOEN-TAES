def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_string = ''
    for char in s:
        if char in alphabet:
            index = (alphabet.index(char) + 12) % 26
            encrypted_string += alphabet[index]
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