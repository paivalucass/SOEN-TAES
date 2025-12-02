def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) if ch.islower() else ch for ch in s])

def decode_shift(s: str):
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) if ch.islower() else ch for ch in s])
import unittest

class Test(unittest.TestCase):
    def test_encode_shift(self):
        self.assertEqual(encode_shift('abcde'), 'fghij')

    def test_decode_shift(self):
        self.assertEqual(decode_shift('fghij'), 'abcde')

if __name__ == '__main__':
    unittest.main()