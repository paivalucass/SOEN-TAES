def check_if_last_char_is_a_letter(txt):
    if len(txt) < 2:
        return False
    last_char = txt[-1]
    second_last_char = txt[-2]
    if last_char.isalpha() and second_last_char == ' ':
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_if_last_char_is_a_letter("apple pie"), False)
        self.assertEqual(check_if_last_char_is_a_letter("apple pi e"), True)
        self.assertEqual(check_if_last_char_is_a_letter("apple pi e "), False)
        self.assertEqual(check_if_last_char_is_a_letter(""), False)

if __name__ == '__main__':
    unittest.main()