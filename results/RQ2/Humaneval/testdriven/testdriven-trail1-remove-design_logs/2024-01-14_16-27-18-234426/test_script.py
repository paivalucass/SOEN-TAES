def check_if_last_char_is_a_letter(txt):
    words = txt.split()
    if len(words) == 0 or (not txt[-1].isalpha() and len(words[-1]) == len(words[-1].strip())):
        return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_if_last_char_is_a_letter('apple pie'), False)
        self.assertEqual(check_if_last_char_is_a_letter('apple pi e'), True)
        self.assertEqual(check_if_last_char_is_a_letter('apple pi e '), False)
        self.assertEqual(check_if_last_char_is_a_letter(''), False)

if __name__ == '__main__':
    unittest.main()