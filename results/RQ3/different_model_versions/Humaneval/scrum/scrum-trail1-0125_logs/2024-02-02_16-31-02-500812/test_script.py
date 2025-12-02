FIX = """
Add more test cases.
"""
def vowels_count(s):
    vowels = 'aeiou'
    s = s.lower()
    count = 0
    for i in range(len(s)):
        if s[i] in vowels or (s[i] == 'y' and i == len(s) - 1):
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test_vowels_count(self):
        self.assertEqual(vowels_count('abcde'), 2)
        self.assertEqual(vowels_count('ACEDY'), 3)
        self.assertEqual(vowels_count('hello'), 2)
        self.assertEqual(vowels_count('world'), 1)
        self.assertEqual(vowels_count('python'), 1)

if __name__ == '__main__':
    unittest.main()