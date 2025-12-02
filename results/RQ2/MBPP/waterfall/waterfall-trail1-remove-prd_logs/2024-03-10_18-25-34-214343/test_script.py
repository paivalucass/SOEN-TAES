def text_lowercase_underscore(text):
    import re
    is_lowercase_underscore = False
    pattern = r'^[a-z]+_[a-z]+$'
    if re.match(pattern, text):
        is_lowercase_underscore = True
    return is_lowercase_underscore
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_lowercase_underscore('aab_cbbbc'), True)

if __name__ == '__main__':
    unittest.main()