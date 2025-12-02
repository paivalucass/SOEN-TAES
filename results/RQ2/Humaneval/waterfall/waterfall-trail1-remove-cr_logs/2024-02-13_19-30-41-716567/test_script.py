def cycpattern_check(a, b):
    if len(a) != len(b):
        return False
    if b in a:
        return True
    for i in range(len(b)):
        if (b in (a[i:] + a[:i])):
            return True
    return False
import unittest

class Test(unittest.TestCase):
    def test_cycpattern_check(self):
        self.assertEqual(cycpattern_check("abcd", "abd"), False)
        self.assertEqual(cycpattern_check("hello", "ell"), True)
        self.assertEqual(cycpattern_check("whassup", "psus"), False)
        self.assertEqual(cycpattern_check("abab", "baa"), True)
        self.assertEqual(cycpattern_check("efef", "eeff"), False)
        self.assertEqual(cycpattern_check("himenss", "simen"), True)

if __name__ == '__main__':
    unittest.main()