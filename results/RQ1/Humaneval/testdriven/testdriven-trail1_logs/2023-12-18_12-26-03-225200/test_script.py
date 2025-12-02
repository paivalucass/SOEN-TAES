def encode_shift(input_string: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    """
    if not input_string.isalpha():
        return "Invalid input"
    
    encoded_string = ""
    for char in input_string:
        shifted_char = chr(((ord(char) + 5 - ord("a")) % 26) + ord("a"))
        encoded_string += shifted_char
    
    return encoded_string

def decode_shift(encoded_string: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    """
    decoded_string = ""
    for char in encoded_string:
        shifted_char = chr(((ord(char) - 5 - ord("a")) % 26) + ord("a"))
        decoded_string += shifted_char
    
    return decoded_string
import unittest

class Test(unittest.TestCase):
    def test_encode_shift(self):
        self.assertEqual(encode_shift('abcde'), 'fghij')
    
    def test_decode_shift(self):
        self.assertEqual(decode_shift('fghij'), 'abcde')

if __name__ == '__main__':
    unittest.main()