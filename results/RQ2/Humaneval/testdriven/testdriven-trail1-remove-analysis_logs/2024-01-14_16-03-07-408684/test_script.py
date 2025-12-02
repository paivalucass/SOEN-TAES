def create_mapping():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    mapping = {}
    for i in range(len(alphabet)):
        new_index = (i + 2) % 26
        mapping[alphabet[i]] = alphabet[new_index]
    return mapping

def encrypt(s):
    mapping = create_mapping()
    encrypted_string = ''
    for char in s:
        if char.isalpha():
            if char.isupper():
                encrypted_string += mapping[char.lower()].upper()
            else:
                encrypted_string += mapping[char]
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