def encode(message):
    encoded_message = ''
    vowels = 'aeiouAEIOU'
    for char in message:
        if char.lower() in vowels:
            encoded_message += chr((ord(char) + 2 - 65) % 26 + 65) if char.isupper() else chr((ord(char) + 2 - 97) % 26 + 97)
        else:
            encoded_message += char.swapcase()
    return encoded_message
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(encode('test'), 'TGST')
        self.assertEqual(encode('This is a message'), 'tHKS KS C MGSSCGG')
        
if __name__ == '__main__':
    unittest.main()