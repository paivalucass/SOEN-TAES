def same_chars(s0: str, s1: str) -> bool:
    if len(s0) != len(s1):
        return False
    char_count = {}
    for char in s0:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in s1:
        if char in char_count:
            char_count[char] -= 1
        else:
            return False
    return all(count == 0 for count in char_count.values())
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