def same_chars(s0: str, s1: str) -> bool:
    # Pre-process the input strings to remove special characters and whitespace
    s0 = ''.join(e for e in s0 if e.isalnum())
    s1 = ''.join(e for e in s1 if e.isalnum())

    # Convert the pre-processed input strings into sets to remove duplicate characters
    s0_set = set(s0)
    s1_set = set(s1)

    # Use built-in set operations for efficient comparison
    return s0_set == s1_set

import unittest

class Test(unittest.TestCase):
    def test_1(self):
        self.assertTrue(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))

    def test_2(self):
        self.assertTrue(same_chars('abcd', 'dddddddabc'))

    def test_3(self):
        self.assertTrue(same_chars('dddddddabc', 'abcd'))

    def test_4(self):
        self.assertFalse(same_chars('eabcd', 'dddddddabc'))

    def test_5(self):
        self.assertFalse(same_chars('abcd', 'dddddddabce'))

    def test_6(self):
        self.assertFalse(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))

if __name__ == '__main__':
    unittest.main()