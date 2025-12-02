def check_if_last_char_is_a_letter(txt):
    if txt.strip() == '':
        return False
    words = txt.split()
    last_word = words[-1]
    last_char = last_word[-1]
    return last_char.isalpha() and not last_char.isalnum()
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_if_last_char_is_a_letter('apple pie'), False)
        self.assertEqual(check_if_last_char_is_a_letter('apple pi e'), True)
        self.assertEqual(check_if_last_char_is_a_letter('apple pi e '), False)
        self.assertEqual(check_if_last_char_is_a_letter(''), False)

if __name__ == '__main__':
    unittest.main()