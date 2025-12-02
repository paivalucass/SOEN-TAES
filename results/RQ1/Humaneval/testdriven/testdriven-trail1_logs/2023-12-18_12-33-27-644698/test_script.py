def encode(message):
    if not message or not message.isalpha():
        return ''

    vowels = "AEIOUaeiou"
    encoded_msg = ""

    for char in message:
        if char.lower() in vowels:
            if char.isupper():
                encoded_msg += chr((ord(char) + 2 - 65) % 26 + 65)
            else:
                encoded_msg += chr((ord(char) + 2 - 97) % 26 + 97)
        else:
            encoded_msg += char.swapcase()

    return encoded_msg
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(encode('test'), 'TGST')
        self.assertEqual(encode('This is a message'), 'tHKS KS C MGSSCGG')

if __name__ == '__main__':
    unittest.main()