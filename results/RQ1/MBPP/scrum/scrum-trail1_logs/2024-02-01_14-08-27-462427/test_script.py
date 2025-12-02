def find_Rotations(s):
    n = len(s)
    for i in range(1, n+1):
        if s[:i] * (n//i) == s:
            return i
    return n
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Rotations('aaaa'), 1)

if __name__ == '__main__':
    unittest.main()