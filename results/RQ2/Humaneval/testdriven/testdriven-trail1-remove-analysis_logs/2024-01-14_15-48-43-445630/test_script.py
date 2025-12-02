from collections import Counter

def same_chars(s0: str, s1: str) -> bool:
    if not isinstance(s0, str) or not isinstance(s1, str):
        return False
    if len(s0) != len(s1):
        return False
    if len(s0) == 0 and len(s1) == 0:
        return True

    count_s0 = Counter(s0)
    count_s1 = Counter(s1)

    return count_s0 == count_s1

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