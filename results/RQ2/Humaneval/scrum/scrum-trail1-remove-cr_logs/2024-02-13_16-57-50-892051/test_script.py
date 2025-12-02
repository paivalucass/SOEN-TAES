def same_chars(s0: str, s1: str):
    set_s0 = set(s0)
    set_s1 = set(s1)

    return set_s0 == set_s1
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