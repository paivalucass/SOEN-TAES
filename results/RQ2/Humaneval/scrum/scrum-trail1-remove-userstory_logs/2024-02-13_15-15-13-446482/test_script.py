def rotateAlphabet(rotation):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated_alphabet = alphabet[rotation:] + alphabet[:rotation]
    return rotated_alphabet

def encrypt(s):
    encrypted_string = ""
    rotation = 2
    for char in s:
        if char.isalpha():
            if char.islower():
                index = ord(char) - ord('a')
                new_index = (index + rotation) % 26
                encrypted_string += rotateAlphabet(rotation)[new_index]
            else:
                index = ord(char) - ord('A')
                new_index = (index + rotation) % 26
                encrypted_string += rotateAlphabet(rotation).upper()[new_index]
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