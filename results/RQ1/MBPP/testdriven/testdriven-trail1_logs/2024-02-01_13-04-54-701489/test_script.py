def first_repeated_char(str1):
    '''Write a python function to find the first repeated character in a given string.
    assert first_repeated_char("abcabc") == "a"'''
    
    if str1 is None or str1 == "":
        raise ValueError("Input string cannot be empty or None")
    
    str1 = str1.lower()
    
    char_freq = {}
    
    for char in str1:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    
    for char in str1:
        if char_freq[char] > 1:
            return char
    
    return None
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(first_repeated_char('abcabc'), 'a')

if __name__ == '__main__':
    unittest.main()