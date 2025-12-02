def encrypt(s):
    if not s.isalpha():
        return "Error: Input string contains non-alphabetic characters"

    encrypted_string = ""
    for char in s:
        if char.islower():
            encrypted_string += chr(((ord(char) - 97 + 2) * 2) % 26 + 97)
        else:
            encrypted_string += chr(((ord(char) - 65 + 2) * 2) % 26 + 65)

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