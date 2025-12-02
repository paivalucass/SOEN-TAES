def check_if_last_char_is_a_letter(txt):
    if len(txt) == 0 or not txt.strip():
        return False  # empty input string
    words = txt.split()
    last_word = words[-1]
    if len(last_word) == 1:
        if last_word.isalpha():
            return True
    elif len(last_word) > 1:
        last_char = last_word[-1]
        if last_char.isalpha() and last_word[-2] == ' ':  # check if last char is an alphabet and not part of a word
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