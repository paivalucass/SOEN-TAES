def check_if_last_char_is_a_letter(txt):
    if not isinstance(txt, str) or txt.strip() == "":
        return False
    elif len(txt) == 1 and txt.isalpha():
        return True
    elif txt[-1].isalpha() and txt[-2] == ' ':
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