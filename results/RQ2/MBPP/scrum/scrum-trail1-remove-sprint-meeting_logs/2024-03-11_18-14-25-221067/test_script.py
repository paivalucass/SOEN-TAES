def is_sublist(l, s):
    for i in range(len(l) - len(s) + 1):
        if l[i:i + len(s)] == s:
            return True
    return False
import unittest

class Test(unittest.TestCase):
    def test_is_sublist(self):
        self.assertEqual(is_sublist([2,4,3,5,7],[3,7]), True)

if __name__ == '__main__':
    unittest.main()