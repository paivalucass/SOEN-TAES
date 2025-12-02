def check_if_last_char_is_a_letter(txt: str) -> bool:
    if not isinstance(txt, str) or len(txt) == 0:
        return False
    txt = txt.strip()
    return txt[-1].isalpha() and (len(txt) == 1 or txt[-2] == ' ')
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_if_last_char_is_a_letter('apple pie'), False)
        self.assertEqual(check_if_last_char_is_a_letter('apple pi e'), True)
        self.assertEqual(check_if_last_char_is_a_letter('apple pi e '), False)
        self.assertEqual(check_if_last_char_is_a_letter(''), False)

if __name__ == '__main__':
    unittest.main()