def text_match_wordz_middle(text):
    words = text.split()
    for word in words:
        if len(word) >= 3:
            if len(word) % 2 != 0:
                if word[len(word)//2] == 'z' and word[0] != 'z' and word[-1] != 'z':
                    return True
            else:
                if (word[len(word)//2-1] == 'z' or word[len(word)//2] == 'z') and word[0] != 'z' and word[-1] != 'z':
                    return True
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_wordz_middle('pythonzabc.'), True)

if __name__ == '__main__':
    unittest.main()