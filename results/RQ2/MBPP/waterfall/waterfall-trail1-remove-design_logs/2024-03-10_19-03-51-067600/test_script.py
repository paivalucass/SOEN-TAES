def text_lowercase_underscore(text):
    import re
    regex_pattern = r'^[a-z]+(_[a-z]+)+$'
    return bool(re.match(regex_pattern, text))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_lowercase_underscore('aab_cbbbc'), True)

if __name__ == '__main__':
    unittest.main()