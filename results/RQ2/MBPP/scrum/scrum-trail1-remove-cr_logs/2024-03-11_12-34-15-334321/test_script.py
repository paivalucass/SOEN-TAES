def is_sublist(l, s):
    if not s:
        return True
    if len(s) > len(l):
        return False
    for i in range(len(l)):
        if l[i] == s[0]:
            if l[i:i+len(s)] == s:
                return True
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_sublist([2,4,3,5,7], [3,7]), False)

if __name__ == '__main__':
    unittest.main()