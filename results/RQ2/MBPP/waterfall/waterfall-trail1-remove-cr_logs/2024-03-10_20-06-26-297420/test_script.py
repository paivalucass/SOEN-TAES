def text_match_wordz(text):
    if text is None or text.strip() == "":
        return False
    
    words = text.split()
    for word in words:
        if 'z' in word:
            return True
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_wordz('pythonz.'), True)

if __name__ == '__main__':
    unittest.main()