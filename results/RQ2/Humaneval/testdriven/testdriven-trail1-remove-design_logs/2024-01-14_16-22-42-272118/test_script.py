def encode(message):
    vowels_mapping = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w'}
    encoded_message = ""
    for char in message:
        if char.isalpha():
            if char.lower() in vowels_mapping:
                encoded_message += vowels_mapping[char.lower()].upper()
            else:
                encoded_message += char.swapcase()
        else:
            encoded_message += char
    return encoded_message
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(encode('test'), 'TGST')
        self.assertEqual(encode('This is a message'), 'tHKS KS C MGSSCGG')

if __name__ == '__main__':
    unittest.main()