def remove_Occ(s, ch):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    start = 0
    end = len(s) - 1
    while start < len(s) and s[start] != ch:
        start += 1
    while end >= 0 and s[end] != ch:
        end -= 1
    
    if start < len(s) and end >= 0:
        if char_count[ch] > 1:
            return s[:start] + s[start+1:end] + s[end+1:]
        else:
            return s[:start] + s[start+1:]
    else:
        return s
import unittest

class Test(unittest.TestCase):
    def test_remove_Occ(self):
        self.assertEqual(remove_Occ("hello", "l"), "heo")

if __name__ == '__main__':
    unittest.main()