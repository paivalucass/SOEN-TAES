def text_lowercase_underscore(text):
    import re
    pattern = r"[a-z]+_[a-z]+"
    if re.search(pattern, text):
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test_lowercase_underscore(self):
        self.assertEqual(text_lowercase_underscore('aab_cbbbc'), True)

if __name__ == '__main__':
    unittest.main()