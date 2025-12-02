def split_Arr(l, n):
    if not l:
        raise ValueError("Input list 'l' should not be empty")
    modified_list = l[n:] + l[:n]
    return modified_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(split_Arr([12,10,5,6,52,36], 2), [5,6,52,36,12,10])

if __name__ == '__main__':
    unittest.main()