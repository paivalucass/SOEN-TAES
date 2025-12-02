def text_match_wordz(text):
    if not isinstance(text, str):
        return "Error: Invalid input type"
    elif text.strip() == '':
        return "Error: Empty input"
    elif 'z' in text:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_wordz('pythonz.'), True)

if __name__ == '__main__':
    unittest.main()