def text_match_wordz(text):
    import re
    words = re.findall(r'\b\w*z\w*\b', text) 
    return len(words) > 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_wordz("pythonz."), True)

if __name__ == '__main__':
    unittest.main()