# Rewritten Code:
def encode_cyclic(s: str) -> str:
    """Returns an encoded string by cycling groups of three characters."""
    # split string to groups. Each of length 3.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """Takes as input a string encoded with the encode_cyclic function. Returns decoded string."""
    # split string to groups. Each of length 3.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:2]) if len(group) == 3 else group for group in groups]
    return "".join(groups)
import unittest

class TestDecodeCyclic(unittest.TestCase):
    def test_decode_cyclic(self):
        self.assertEqual(decode_cyclic('bcdae'), 'abcde')
        self.assertEqual(decode_cyclic('bcad'), 'abcd')
        self.assertEqual(decode_cyclic('bcdaefg'), 'abcdefg')

if __name__ == '__main__':
    unittest.main()