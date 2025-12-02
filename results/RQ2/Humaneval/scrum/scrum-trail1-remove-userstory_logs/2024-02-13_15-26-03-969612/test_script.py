def check_if_last_char_is_a_letter(txt):
    import re
    if txt.strip() == "":
        return False
    last_char = txt.strip()[-1]
    if re.match("[a-zA-Z]", last_char):
        if re.search(r"\s", txt[-2]):
            return True
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