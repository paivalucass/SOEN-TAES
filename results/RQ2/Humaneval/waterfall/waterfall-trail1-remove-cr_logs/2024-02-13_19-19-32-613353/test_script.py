def same_chars(s0: str, s1: str):
    s0 = ''.join(sorted(e for e in s0.lower() if e.isalnum()))
    s1 = ''.join(sorted(e for e in s1.lower() if e.isalnum()))
    return s0 == s1
import unittest

class Test(unittest.TestCase):
    def test_same_chars(self):
        self.assertTrue(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))
        self.assertTrue(same_chars('abcd', 'dddddddabc'))
        self.assertTrue(same_chars('dddddddabc', 'abcd'))
        self.assertFalse(same_chars('eabcd', 'dddddddabc'))
        self.assertFalse(same_chars('abcd', 'dddddddabce'))
        self.assertFalse(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))

if __name__ == '__main__':
    unittest.main()