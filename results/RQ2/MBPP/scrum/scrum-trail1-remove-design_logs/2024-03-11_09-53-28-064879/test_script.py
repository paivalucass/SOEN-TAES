def text_lowercase_underscore(text):
    if len(text) == 0:
        return False
    if text[-1] == '_':
        return False
    words = text.split('_')
    for word in words:
        if not word.islower():
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_lowercase_underscore('aab_cbbbc'), True)

if __name__ == '__main__':
    unittest.main()