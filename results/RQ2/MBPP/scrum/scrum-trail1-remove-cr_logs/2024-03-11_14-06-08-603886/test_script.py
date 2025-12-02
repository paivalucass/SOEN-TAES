import re

def text_starta_endb(text):
    if text is None or len(text) == 0:
        return False
    
    start_pattern = '^a.*'
    end_pattern = '.*b$'
    
    if re.match(start_pattern, text) and re.match(end_pattern, text):
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(text_starta_endb("aabbbb"))

if __name__ == '__main__':
    unittest.main()