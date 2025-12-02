def text_lowercase_underscore(text):
    if not text:
        return False
    for i in range(len(text)-2):
        if text[i].islower() and text[i+1] == '_' and text[i+2].islower():
            return True
    return False
import unittest

class Test(unittest.TestCase):
    def test_lowercase_underscore(self):
        self.assertEqual(text_lowercase_underscore('aab_cbbbc'), True)

if __name__ == '__main__':
    unittest.main()