def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([shift_char(ch, 5) for ch in s])

def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([shift_char(ch, -5) for ch in s])

def shift_char(ch: str, shift_amount: int):
    if ch.islower():
        return chr(((ord(ch) + shift_amount - ord("a")) % 26) + ord("a"))
    elif ch.isupper():
        return chr(((ord(ch) + shift_amount - ord("A")) % 26) + ord("A"))
    else:
        return ch
import unittest

class Test(unittest.TestCase):
    def test_encode_shift(self):
        self.assertEqual(encode_shift('abc'), 'fgh')

    def test_decode_shift(self):
        self.assertEqual(decode_shift('fgh'), 'abc')

if __name__ == '__main__':
    unittest.main()