def encode(message):
    if not isinstance(message, str):
        raise TypeError("Input message must be a string")
    
    def swap_case(message):
        result = ""
        for char in message:
            if char.isalpha():
                if char.islower():
                    result += char.upper()
                else:
                    result += char.lower()
            else:
                result += char
        return result

    def replace_vowels(message):
        vowels = "aeiouAEIOU"
        result = ""
        for char in message:
            if char in vowels:
                if char.islower():
                    result += chr((ord(char) - 97 + 2) % 26 + 97)
                else:
                    result += chr((ord(char) - 65 + 2) % 26 + 65)
            else:
                result += char
        return result

    swapped_message = swap_case(message)
    encoded_message = replace_vowels(swapped_message)
    return encoded_message
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(encode('test'), 'TGST')
        self.assertEqual(encode('This is a message'), 'tHKS KS C MGSSCGG')

if __name__ == '__main__':
    unittest.main()