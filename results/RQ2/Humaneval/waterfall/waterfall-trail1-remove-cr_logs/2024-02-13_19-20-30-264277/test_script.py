FIX = """
Add more test cases.
"""

def vowels_count(s):
    vowels = "aeiou"
    count = 0

    for i in range(len(s)):
        if s[i].lower() in vowels:
            if s[i].lower() == 'y' and i == len(s) - 1:
                count += 1
            elif s[i].lower() != 'y':
                count += 1
            elif s[i].lower() == 'y' and i != len(s) - 1:
                count = 0

    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(vowels_count('abcde'), 2)
        self.assertEqual(vowels_count('ACEDY'), 3)
        self.assertEqual(vowels_count('hello'), 2)
        self.assertEqual(vowels_count('aeiou'), 5)

if __name__ == '__main__':
    unittest.main()