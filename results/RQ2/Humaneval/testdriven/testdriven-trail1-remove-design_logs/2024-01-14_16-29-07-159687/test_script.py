def cycpattern_check(a, b):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True
    """

    rotations = [b[i:] + b[:i] for i in range(len(b))]  # Generate all rotations of the string
    for rotation in rotations:
        if rotation in a:
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