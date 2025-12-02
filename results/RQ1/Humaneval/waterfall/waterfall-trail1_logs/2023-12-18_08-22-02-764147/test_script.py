def encode(message):
    encoded_message = ""
    vowels = 'aeiouAEIOU'
    for char in message:
        if not char.isalpha():
            raise ValueError('Input should only contain letters')
        if char in vowels:
            char_index = (ord(char.lower()) - ord('a') + 2) % 26
            encoded_char = chr(ord('a') + char_index)
            if char.isupper():
                encoded_message += encoded_char.upper()
            else:
                encoded_message += encoded_char
        else:
            encoded_message += char.swapcase()

    return encoded_message
import unittest

class Test(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(encode('test'), 'TGST')
        self.assertEqual(encode('This is a message'), 'tHKS KS C MGSSCGG')

if __name__ == '__main__':
    unittest.main()