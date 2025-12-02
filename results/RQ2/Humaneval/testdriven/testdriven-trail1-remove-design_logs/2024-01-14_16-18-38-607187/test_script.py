def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    """
    if not isinstance(s, str):
        raise ValueError("Input should be a string")
    # Add comments to explain the logic behind the encoding process
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    """
    if not isinstance(s, str):
        raise ValueError("Input should be a string")
    # Add comments to explain the logic behind the decoding process
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])
import unittest

class Test(unittest.TestCase):
    def test_encode_shift(self):
        self.assertEqual(encode_shift('hello'), 'mjqqt')
    
    def test_decode_shift(self):
        self.assertEqual(decode_shift('mjqqt'), 'hello')

if __name__ == '__main__':
    unittest.main()