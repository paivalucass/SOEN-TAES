def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    """
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    groups = [(group[1] + group[2] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)
import unittest

class Test(unittest.TestCase):
    def test_encode_cyclic(self):
        self.assertEqual(encode_cyclic('abcdefgh'), 'bcadefgh')
        self.assertEqual(encode_cyclic('abcdef'), 'bcadef')
        self.assertEqual(encode_cyclic('abc'), 'abc')

    def test_decode_cyclic(self):
        self.assertEqual(decode_cyclic('bcadefgh'), 'abcdefgh')
        self.assertEqual(decode_cyclic('bcadef'), 'abcdef')
        self.assertEqual(decode_cyclic('abc'), 'abc')

if __name__ == '__main__':
    unittest.main()