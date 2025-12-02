def text_match_wordz(text):
    import re  # moving the import statement outside of the function
    pattern = r'\b\w*z\w*\b'
    match = re.search(pattern, text)
    if match:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_wordz('pythonz.'), True)

if __name__ == '__main__':
    unittest.main()