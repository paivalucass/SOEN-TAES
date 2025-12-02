def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    """
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    encoded_groups = [group[1:] + group[0] if len(group) == 3 else group for group in groups]
    return ''.join(encoded_groups)

def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    decoded_groups = [group[-1] + group[:2] if len(group) == 3 else group for group in groups]
    return ''.join(decoded_groups)
import unittest

class Test(unittest.TestCase):
    def test_encode_cyclic(self):
        self.assertEqual(encode_cyclic('abc'), 'bca')
        self.assertEqual(encode_cyclic('abcdef'), 'bcadef')

    def test_decode_cyclic(self):
        self.assertEqual(decode_cyclic('bca'), 'abc')
        self.assertEqual(decode_cyclic('bcadef'), 'abcdef')

if __name__ == '__main__':
    unittest.main()