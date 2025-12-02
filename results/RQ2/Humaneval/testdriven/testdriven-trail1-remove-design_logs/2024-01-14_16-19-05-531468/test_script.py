def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    """
    return sorted(s0) == sorted(s1)

import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertTrue(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))

    def test2(self):
        self.assertTrue(same_chars('abcd', 'dddddddabc'))

    def test3(self):
        self.assertTrue(same_chars('dddddddabc', 'abcd'))

    def test4(self):
        self.assertFalse(same_chars('eabcd', 'dddddddabc'))

    def test5(self):
        self.assertFalse(same_chars('abcd', 'dddddddabce'))

    def test6(self):
        self.assertFalse(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))

if __name__ == '__main__':
    unittest.main()