import re

def check_if_last_char_is_a_letter(txt):
    if not txt:
        return False
    
    words = txt.split()
    last_word = words[-1] if words else ''
    
    last_char = last_word.strip()[-1] if last_word.strip() else ''
    
    if re.search(r'[a-zA-Z]', last_char):
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_if_last_char_is_a_letter('apple pie'), False)
        self.assertEqual(check_if_last_char_is_a_letter('apple pi e'), True)
        self.assertEqual(check_if_last_char_is_a_letter('apple pi e '), False)
        self.assertEqual(check_if_last_char_is_a_letter(''), False)

if __name__ == '__main__':
    unittest.main()