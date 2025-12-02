def text_match_wordz(text: str) -> bool:
    if not isinstance(text, str):
        raise ValueError("Input text must be a valid string")

    import re
    pattern = re.compile(r'\b\w*z\w*\b', re.IGNORECASE)
    return bool(pattern.search(text))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_wordz('pythonz.'), True)

if __name__ == '__main__':
    unittest.main()