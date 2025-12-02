def encrypt(s):
    if not isinstance(s, str):
        return "Error: Input is not a string"
    if len(s) == 0:
        return ""
    encrypted = ""
    for char in s:
        if char.isalpha():
            if char.islower():
                encrypted += chr((ord(char) - 97 + 2*2) % 26 + 97)
            else:
                encrypted += chr((ord(char) - 65 + 2*2) % 26 + 65)
    return encrypted

import unittest

class Test(unittest.TestCase):
    def test_encrypt(self):
        self.assertEqual(function_under_test('hi'), 'lm')
        self.assertEqual(function_under_test('asdfghjkl'), 'ewhjklnop')
        self.assertEqual(function_under_test('gf'), 'kj')
        self.assertEqual(function_under_test('et'), 'ix')

if __name__ == '__main__':
    unittest.main()