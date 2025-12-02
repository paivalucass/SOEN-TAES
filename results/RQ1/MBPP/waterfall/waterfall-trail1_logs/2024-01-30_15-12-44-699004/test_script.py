def text_match_three(text):
    import re

    if not isinstance(text, str):
        raise ValueError("Input must be a string")

    pattern = r'ab{3}'
    if re.search(pattern, text):
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(text_match_three("abbb"))
        self.assertFalse(text_match_three("ac"))
        # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()