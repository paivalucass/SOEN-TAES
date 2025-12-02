def text_lowercase_underscore(text):
    import re
    if text is None or len(text) == 0:
        return False
    pattern = r'^[a-z]+_[a-z]+$'
    return bool(re.match(pattern, text))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_lowercase_underscore("aab_cbbbc"), True)

if __name__ == '__main__':
    unittest.main()