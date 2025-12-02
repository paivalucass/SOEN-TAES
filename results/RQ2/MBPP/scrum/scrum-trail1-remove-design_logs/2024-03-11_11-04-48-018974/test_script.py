def text_match_wordz_middle(text):
    for word in text.split():
        if len(word) > 2 and 'z' in word[1:-1]:
            return True
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_wordz_middle("pythonzabc."), True)

if __name__ == '__main__':
    unittest.main()