def encrypt(s, shift_value=2):
    encrypted_string = ""
    for char in s:
        if char.isalpha():
            if char.islower():
                encrypted_char = chr((ord(char) - 97 + shift_value) % 26 + 97)
            else:
                encrypted_char = chr((ord(char) - 65 + shift_value) % 26 + 65)
            encrypted_string += encrypted_char
        else:
            encrypted_string += char
    return encrypted_string
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test('hi'), 'lm')
        self.assertEqual(function_under_test('asdfghjkl'), 'ewhjklnop')
        self.assertEqual(function_under_test('gf'), 'kj')
        self.assertEqual(function_under_test('et'), 'ix')

if __name__ == '__main__':
    unittest.main()