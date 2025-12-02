def encode(message):
    encoded_message = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                char = char.upper()
            else:
                char = char.lower()
            if char in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                char = chr(ord(char) + 2)
        encoded_message += char
    return encoded_message
import unittest

class Test(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(encode('test'), 'TGST')
        self.assertEqual(encode('This is a message'), 'tHKS KS C MGSSCGG')

if __name__ == '__main__':
    unittest.main()