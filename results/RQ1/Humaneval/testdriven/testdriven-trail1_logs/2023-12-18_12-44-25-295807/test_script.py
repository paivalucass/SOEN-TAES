def cycpattern_check(input_string, substring):
    if not input_string or not substring:
        return False
    if len(input_string) != len(substring):
        return False
    input_string += input_string
    if substring in input_string:
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