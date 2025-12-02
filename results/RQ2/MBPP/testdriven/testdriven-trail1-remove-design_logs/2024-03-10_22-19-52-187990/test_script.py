def text_starta_endb(text):
    # Write a function that matches a string that has an 'a' followed by anything, ending in 'b'.
    # assert text_starta_endb("aabbbb")
    import re
    pattern = r'a.*b$'
    if re.match(pattern, text):
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(text_starta_endb('aabbbb'))

if __name__ == '__main__':
    unittest.main()