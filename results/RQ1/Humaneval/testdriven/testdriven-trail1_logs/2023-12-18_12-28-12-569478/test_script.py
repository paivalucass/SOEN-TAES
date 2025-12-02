FIX = """
Add more test cases.
"""

def vowels_count(s):
    vowels = 'aeiou'
    count = 0
    s_lower = s.lower()
    for i in range(len(s_lower)):
        if s_lower[i] in vowels:
            if s_lower[i] != 'y' or i == len(s_lower) - 1:
                count += 1
    return count

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(vowels_count('a'), 1)
        self.assertEqual(vowels_count('abcde'), 2)
        self.assertEqual(vowels_count('ACEDY'), 3)
        self.assertEqual(vowels_count('hello'), 2)
        self.assertEqual(vowels_count('Python'), 2)

if __name__ == '__main__':
    unittest.main()