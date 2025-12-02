def text_match_three(text):
    import re
    pattern = 'abbb'
    if re.search(pattern, text):
        return "Match found"
    else:
        return "No match found"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(text_match_three('ac'))

if __name__ == '__main__':
    unittest.main()