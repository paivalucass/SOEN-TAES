def split_Arr(l, n):
    if not l:
        raise ValueError("Input list is empty")
    if n < 0 or n >= len(l):
        raise ValueError("Value of 'n' is out of range")

    return l[n:] + l[:n]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(split_Arr([12,10,5,6,52,36], 2), [5,6,52,36,12,10])

if __name__ == '__main__':
    unittest.main()