def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:2]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    return s[-1] + s[:-1]
import unittest

class Test(unittest.TestCase):
    def test_encode_cyclic(self):
        self.assertEqual(encode_cyclic('abcde'), 'bcdea')
        self.assertEqual(encode_cyclic('abcdef'), 'bcdaef')

    def test_decode_cyclic(self):
        self.assertEqual(decode_cyclic('bcdea'), 'abcde')
        self.assertEqual(decode_cyclic('bcdaef'), 'abcdef')

if __name__ == '__main__':
    unittest.main()