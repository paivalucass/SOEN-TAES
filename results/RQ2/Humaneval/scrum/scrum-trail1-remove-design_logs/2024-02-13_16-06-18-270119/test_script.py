def same_chars(s0: str, s1: str):
    map_s0 = {char: s0.count(char) for char in set(s0)}
    map_s1 = {char: s1.count(char) for char in set(s1)}
    return map_s0 == map_s1
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