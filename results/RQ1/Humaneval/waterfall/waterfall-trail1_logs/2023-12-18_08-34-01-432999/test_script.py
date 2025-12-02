def cycpattern_check(a, b):
    def compute_lps_array(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = compute_lps_array(b + '$' + b)
    i = 0
    j = 0
    while i < len(a):
        if b[j] == a[i]:
            i += 1
            j += 1
            if j == len(b):
                return True
        elif i < len(a) and b[j] != a[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(cycpattern_check("abcd", "abd"), False)
        self.assertEqual(cycpattern_check("hello", "ell"), True)
        self.assertEqual(cycpattern_check("whassup", "psus"), False)
        self.assertEqual(cycpattern_check("abab", "baa"), True)
        self.assertEqual(cycpattern_check("efef", "eeff"), False)
        self.assertEqual(cycpattern_check("himenss", "simen"), True)

if __name__ == '__main__':
    unittest.main()