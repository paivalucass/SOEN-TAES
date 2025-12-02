def text_starta_endb(text):
    import re
    if text is None or text == '':
        return False  
    pattern = r'a.*b$'  
    if re.search(pattern, text):
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(text_starta_endb("aabbbb"))

if __name__ == '__main__':
    unittest.main()