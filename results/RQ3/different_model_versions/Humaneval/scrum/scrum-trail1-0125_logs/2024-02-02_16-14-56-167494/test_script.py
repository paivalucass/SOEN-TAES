def encode_cyclic(s: str):
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    groups = [(group[2] + group[:2]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    groups = [(group[1] + group[2] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)
import unittest

class Test(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(encode_cyclic('abcde'), 'bcaed')

    def test_decode(self):
        self.assertEqual(decode_cyclic('bcaed'), 'abcde')

if __name__ == '__main__':
    unittest.main()