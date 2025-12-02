def text_lowercase_underscore(text):
    import re
    if not isinstance(text, str):
        return "Error handling"
    pattern = r'\b[a-z]+_[a-z]+\b'
    if re.search(pattern, text):
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_lowercase_underscore('aab_cbbbc'), True)

if __name__ == '__main__':
    unittest.main()