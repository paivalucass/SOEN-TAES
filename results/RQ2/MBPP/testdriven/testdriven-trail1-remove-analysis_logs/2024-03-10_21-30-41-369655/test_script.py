def text_starta_endb(text):
    import re
    pattern = "a.*?b"  # More specific regular expression pattern to match 'a' followed by anything, ending in 'b'
    match = re.search(pattern, text)  # Check if the input string matches the pattern
    
    if match:  # If there is a match
        return True
    else:  # If there is no match
        return False
import unittest

class Test(unittest.TestCase):
    def test_text_starta_endb(self):
        self.assertTrue(text_starta_endb('aabbbb'))

if __name__ == '__main__':
    unittest.main()