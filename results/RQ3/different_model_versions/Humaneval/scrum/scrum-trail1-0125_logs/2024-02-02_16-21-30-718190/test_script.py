def encode(message):
    encoded_message = ''
    vowels = 'aeiouAEIOU'
    for char in message:
        if char.isalpha():
            if char in vowels:
                encoded_message += chr((ord(char) + 2 - ord('a')) % 26 + ord('a')).swapcase()
            else:
                encoded_message += char.swapcase()
        else:
            encoded_message += char
    return encoded_message
import unittest

class Test(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(encode('test'), 'TGST')
        self.assertEqual(encode('This is a message'), 'tHKS KS C MGSSCGG')

if __name__ == '__main__':
    unittest.main()