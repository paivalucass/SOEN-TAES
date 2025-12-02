def encode_shift(s: str) -> str:
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) if ch.isalpha() else ch for ch in s])

def decode_shift(s: str) -> str:
    decoded_str = ""
    for ch in s:
        if ch.isalpha():
            decoded_str += chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a"))
        else:
            decoded_str += ch
    return decoded_str
import unittest

class Test(unittest.TestCase):
    def test_encode_shift(self):
        self.assertEqual(encode_shift('abc'), 'fgh')
        self.assertEqual(encode_shift('xyz'), 'cde')

    def test_decode_shift(self):
        self.assertEqual(decode_shift('fgh'), 'abc')
        self.assertEqual(decode_shift('cde'), 'xyz')

if __name__ == '__main__':
    unittest.main()