def encode(message):
    vowels = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w'}
    encoded_message = ""
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                encoded_message += vowels[char.lower()].upper()
            else:
                if char.islower():
                    encoded_message += char.upper()
                else:
                    encoded_message += char.lower()
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