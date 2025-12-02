def encode_shift(s: str) -> str:
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    decoded = ""
    for ch in s:
        if ch.isalpha():
            shifted = chr((ord(ch.lower()) - ord('a') + 5) % 26 + ord('a'))
            decoded += shifted.upper() if ch.isupper() else shifted
        else:
            decoded += ch
    return decoded


def decode_shift(s: str) -> str:
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    encoded = ""
    for ch in s:
        if ch.isalpha():
            shifted = chr((ord(ch.lower()) - ord('a') - 5) % 26 + ord('a'))
            encoded += shifted.upper() if ch.isupper() else shifted
        else:
            encoded += ch
    return encoded
import unittest

class TestEncodeDecode(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(encode_shift('abc'), 'fgh')
        self.assertEqual(encode_shift('xyz'), 'cde')
        self.assertEqual(encode_shift('hello world'), 'mjqqt btwqi')
    
    def test_decode(self):
        self.assertEqual(decode_shift('fgh'), 'abc')
        self.assertEqual(decode_shift('cde'), 'xyz')
        self.assertEqual(decode_shift('mjqqt btwqi'), 'hello world')

if __name__ == '__main__':
    unittest.main()