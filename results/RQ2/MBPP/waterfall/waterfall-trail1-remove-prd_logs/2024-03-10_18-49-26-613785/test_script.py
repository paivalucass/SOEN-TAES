import re

def text_match_three(text):
    if not isinstance(text, str):
        raise TypeError("Input is not a valid string")

    pattern = r"ab{3}"
    match = re.search(pattern, text)

    if match:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(text_match_three("abb"))
        self.assertFalse(text_match_three("ac"))

if __name__ == '__main__':
    unittest.main()