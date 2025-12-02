def encrypt(s):
    if not s or not s.isalpha():
        return "Invalid input. Please enter a non-empty string with alphabetic characters only."

    encrypted_string = ""
    for char in s:
        if char.islower():
            encrypted_string += chr(((ord(char) - ord('a') + 2*2) % 26) + ord('a'))
        else:
            encrypted_string += chr(((ord(char) - ord('A') + 2*2) % 26) + ord('A'))
    
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