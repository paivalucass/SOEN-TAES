import re

def text_match_zero_one(text):
    pattern = r'a(b+)'
    match = re.match(pattern, text)
    return bool(match)

# Test cases
assert text_match_zero_one("") == False
assert text_match_zero_one("ab") == True
assert text_match_zero_one("a") == False
assert text_match_zero_one("c") == False
assert text_match_zero_one("ac") == False
import re
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_zero_one('ac'), False)

if __name__ == '__main__':
    unittest.main()