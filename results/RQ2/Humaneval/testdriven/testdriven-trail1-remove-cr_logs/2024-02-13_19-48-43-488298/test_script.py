def encode(message):
    if not message or not message.isalpha():
        raise ValueError("Input message should not be empty and should only contain letters.")
    
    vowels = 'aeiouAEIOU'
    encoded_message = ""
    
    for char in message:
        if char.lower() in vowels:
            if char.islower():
                encoded_message += chr((ord(char) - 97 + 2) % 26 + 65)
            else:
                encoded_message += chr((ord(char) - 65 + 2) % 26 + 65)
        else:
            if char.islower():
                encoded_message += char.upper()
            else:
                encoded_message += char.lower()
    
    return encoded_message
import unittest

class Test(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(encode('test'), 'TGST')
        self.assertEqual(encode('This is a message'), 'tHKS KS C MGSSCGG')

if __name__ == '__main__':
    unittest.main()