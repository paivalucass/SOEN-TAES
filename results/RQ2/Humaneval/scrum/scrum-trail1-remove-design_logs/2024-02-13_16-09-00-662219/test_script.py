FIX = """
Add more test cases.
"""

def vowels_count(s):
    if not isinstance(s, str) or len(s) == 0:
        return 0
    
    s = s.lower()
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for i in range(len(s)):
        if s[i] in vowels:
            count += 1
        elif i == len(s)-1 and s[i] == 'y':
            count += 1
            
    return count
import unittest

class Test(unittest.TestCase):
    def test_vowels_count(self):
        self.assertEqual(vowels_count('abcde'), 2)
        self.assertEqual(vowels_count('ACEDY'), 3)
        self.assertEqual(vowels_count('hello'), 2)
        self.assertEqual(vowels_count('python'), 1)

if __name__ == '__main__':
    unittest.main()