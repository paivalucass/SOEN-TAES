def encode(message):
    encoded_message = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                encoded_message += char.upper()
            else:
                encoded_message += char.lower()
        else:
            encoded_message += char
    vowels = "aeiouAEIOU"
    for vowel in vowels:
        encoded_message = encoded_message.replace(vowel, chr(ord(vowel) + 2))
    return encoded_message
import unittest

class Test(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(encode('test'), 'TGST')
        self.assertEqual(encode('This is a message'), 'tHKS KS C MGSSCGG')

if __name__ == '__main__':
    unittest.main()