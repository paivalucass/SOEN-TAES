def text_starta_endb(text):
    import re
    pattern = r'a.*b$'
    return bool(re.search(pattern, text))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(text_starta_endb("aabbbb"))

if __name__ == '__main__':
    unittest.main()