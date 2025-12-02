FIX = """
Add more test cases.
"""

def vowels_count(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for i in range(len(s)):
        if s[i] in vowels:
            count += 1
    if s[-1].lower() == 'y' and s[-2] not in vowels:
        count += 1
    return count

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(vowels_count('abcde'), 2)
        self.assertEqual(vowels_count('ACEDY'), 3)
        self.assertEqual(vowels_count('hello'), 2)
        self.assertEqual(vowels_count('world'), 1)

if __name__ == '__main__':
    unittest.main()