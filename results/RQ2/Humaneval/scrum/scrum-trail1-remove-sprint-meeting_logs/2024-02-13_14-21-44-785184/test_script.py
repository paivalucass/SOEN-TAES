from re import search

def check_if_last_char_is_a_letter(txt):
    if not isinstance(txt, str):
        return "Input is not a string"

    pattern = r'\b[a-zA-Z]\b'
    match = search(pattern, txt)

    if match and match.span()[1] == len(txt):
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