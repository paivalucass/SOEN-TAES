def text_lowercase_underscore(text):
    return '_' in text and all(c.islower() for c in text.split('_'))
import unittest

class Test(unittest.TestCase):
    def test_lowercase_underscore(self):
        self.assertEqual(text_lowercase_underscore("aab_cbbbc"), True)

if __name__ == '__main__':
    unittest.main()