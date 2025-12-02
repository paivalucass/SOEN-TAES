def encode(message):
    def swap_case(char):
        if char.islower():
            return char.upper()
        else:
            return char.lower()
    
    def replace_vowels(char):
        if char.lower() in ['a', 'e', 'i', 'o', 'u']:
            return chr((ord(char) + 2 - 97) % 26 + 97)
        else:
            return char
    
    encodedMessage = ""
    
    for char in message:
        if char.isalpha():
            char = swap_case(char)
            char = replace_vowels(char)
            encodedMessage += char
        else:
            encodedMessage += char
    
    return encodedMessage
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(encode('test'), 'TGST')
        self.assertEqual(encode('This is a message'), 'tHKS KS C MGSSCGG')

if __name__ == '__main__':
    unittest.main()