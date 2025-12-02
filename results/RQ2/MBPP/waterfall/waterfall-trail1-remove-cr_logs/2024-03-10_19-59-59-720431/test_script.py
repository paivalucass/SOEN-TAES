def text_match_two_three(text):
    if len(text) < 3:
        return False
    
    for i in range(len(text) - 2):
        if text[i] == 'a':
            if text[i+1:i+3] == 'bb' or (i+3 < len(text) and text[i+1:i+4] == 'bbb'):
                return True
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_two_three('ac'), False)

if __name__ == '__main__':
    unittest.main()