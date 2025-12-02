def text_match_wordz_middle(text):
    if len(text) < 3:
        return False
    
    for i in range(1, len(text) - 1):
        if text[i] == 'z':
            return True
    
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_wordz_middle('pythonzabc.'), True)

if __name__ == '__main__':
    unittest.main()