FIX = """
# Test Cases:
def test_vowels_count():
    assert vowels_count('aeiou') == 5
    assert vowels_count('a1e2i3o4u5') == 5
    assert vowels_count('') == 0
    assert vowels_count('xyz') == 0
    assert vowels_count(None) == 0  # Error/Exception handling
    assert vowels_count('aeiouaeiouaeiou') == 15
    assert vowels_count('bcdfghjklmnpqrstvwxyz') == 0
    assert vowels_count('!@#$%^&123456') == 0
    assert vowels_count('aeiouabc') == 5
"""

def vowels_count(s):
    if s is None:
        return 0  # Error/Exception handling
    count = 0
    vowels = 'aeiou'
    for char in s.lower():
        if char in vowels:
            count += 1
    if s[-1].lower() == 'y':
        count += 1
    return count

# Add more test cases.
"""
def test_vowels_count():
    assert vowels_count('abcde') == 2
    assert vowels_count('ACEDY') == 3
    assert vowels_count('aeiou') == 5
    assert vowels_count('a1e2i3o4u5') == 5
    assert vowels_count('') == 0
    assert vowels_count('xyz') == 0
    assert vowels_count('aeiouaeiouaeiou') == 15
    assert vowels_count('bcdfghjklmnpqrstvwxyz') == 0
    assert vowels_count('!@#$%^&123456') == 0
    assert vowels_count('aeiouabc') == 5
"""

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(vowels_count('a'), 1)
        self.assertEqual(vowels_count('abcde'), 2)
        self.assertEqual(vowels_count('ACEDY'), 3)

if __name__ == '__main__':
    unittest.main()