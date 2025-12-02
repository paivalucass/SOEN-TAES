def text_starta_endb(text):
    import re
    if not isinstance(text, str):
        raise ValueError("Input text must be a string")

    pattern = re.compile(r'a.*b$')
    match = pattern.match(text)
    return bool(match)
import unittest

class Test(unittest.TestCase):
    def test_starta_endb(self):
        self.assertTrue(text_starta_endb("aabbbb"))

if __name__ == '__main__':
    unittest.main()