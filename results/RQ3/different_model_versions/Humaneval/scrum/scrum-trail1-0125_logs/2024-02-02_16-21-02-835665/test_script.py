def encrypt(s):
    if not isinstance(s, str) or not s:
        return "Error: Input must be a non-empty string"
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    encrypted = ""
    for char in s:
        if char.isalpha():
            index = (alphabet.index(char) + 4) % 26
            encrypted += alphabet[index]
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