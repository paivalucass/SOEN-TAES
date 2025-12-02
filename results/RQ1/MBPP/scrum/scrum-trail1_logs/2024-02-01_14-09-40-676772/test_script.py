def text_lowercase_underscore(text):
    return all(map(str.islower, text.split('_')))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_lowercase_underscore('aab_cbbbc'), True)

if __name__ == '__main__':
    unittest.main()