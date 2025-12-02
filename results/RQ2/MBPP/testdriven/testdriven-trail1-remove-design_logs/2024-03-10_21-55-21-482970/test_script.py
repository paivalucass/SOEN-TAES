def text_lowercase_underscore(text):
    if text is None or "_" not in text:
        return False
    segments = text.split("_")
    for segment in segments:
        if not segment.islower():
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test_text_lowercase_underscore(self):
        self.assertEqual(text_lowercase_underscore("aab_cbbbc"), True)

if __name__ == '__main__':
    unittest.main()