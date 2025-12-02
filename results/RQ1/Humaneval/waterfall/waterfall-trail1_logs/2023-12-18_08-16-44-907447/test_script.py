FIX = """
Add more test cases.
"""

def vowels_count(s):
    vowels = 'aeiou'
    count = 0
    s = s.lower()
    for char in s:
        if char in vowels:
            count += 1
    if s.endswith('y') and count > 0:
        count -= 1
    return count

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(vowels_count('a'), 1)
        self.assertEqual(vowels_count('abcde'), 2)
        self.assertEqual(vowels_count('ACEDY'), 3)

if __name__ == '__main__':
    unittest.main()