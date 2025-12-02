def split_Arr(l, n):
    if not isinstance(l, list):
        raise TypeError("Input 'l' should be a valid list type")

    if len(l) == 0 or n >= len(l) or n < 0:
        return l

    return l[n:] + l[:n]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(split_Arr([12,10,5,6,52,36], 2), [5,6,52,36,12,10])

if __name__ == '__main__':
    unittest.main()