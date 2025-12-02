def text_match_wordz(text):
    """
    This function checks if any word in the given text contains 'z'.
    """
    import re
    words = re.findall(r'\b\w+z\w*\b', text)
    if words:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_wordz('pythonz.'), True)

if __name__ == '__main__':
    unittest.main()