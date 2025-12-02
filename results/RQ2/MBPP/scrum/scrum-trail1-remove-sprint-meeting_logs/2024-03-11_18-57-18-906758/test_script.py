def first_repeated_char(str1):
    from collections import defaultdict
    if not str1 or len(str1) < 2:
        return "Input string should have at least 2 characters"
    
    char_count = defaultdict(int)
    for char in str1:
        char_count[char] += 1
        if char_count[char] > 1:
            return char
    
    return None
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(first_repeated_char('abcabc'), 'a')

if __name__ == '__main__':
    unittest.main()