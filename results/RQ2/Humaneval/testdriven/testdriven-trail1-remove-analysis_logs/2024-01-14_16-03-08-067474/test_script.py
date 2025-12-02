def encode(message):
    if not isinstance(message, str) or len(message) == 0:
        return "Invalid input"
    
    result = ""
    vowels = "aeiouAEIOU"
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                if char.islower():
                    result += chr((ord(char) + 2 - 97) % 26 + 97)
                else:
                    result += chr((ord(char) + 2 - 65) % 26 + 65)
            else:
                result += char.swapcase()
        else:
            result += char
    
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(encode('test'), 'TGST')
        self.assertEqual(encode('This is a message'), 'tHKS KS C MGSSCGG')

if __name__ == '__main__':
    unittest.main()