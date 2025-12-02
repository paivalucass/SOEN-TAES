def cycpattern_check(a, b):
    def is_rotation(s1, s2):
        if len(s1) != len(s2):
            return False
        return s1 in (s2 + s2)

    if len(b) > len(a):
        return False

    for i in range(len(a) - len(b) + 1):
        if is_rotation(a[i:i + len(b)], b):
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