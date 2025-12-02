def encode(message):
    def is_vowel(char):
        return char.lower() in 'aeiou'

    def encode_char(char):
        if char.isalpha():
            if is_vowel(char):
                return chr((ord(char) + 2 - 97) % 26 + 97).swapcase()
            else:
                return char.swapcase()
        else:
            return char

    encoded_message = ""
    for char in message:
        encoded_message += encode_char(char)

    return encoded_message
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(encode('test'), 'TGST')
        self.assertEqual(encode('This is a message'), 'tHKS KS C MGSSCGG')

if __name__ == '__main__':
    unittest.main()