def check_if_last_char_is_a_letter(txt):
    if len(txt) == 0 or txt[-1].isalpha() and (len(txt) == 1 or not txt[-2].isalpha()):
        return True
    return False
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(check_if_last_char_is_a_letter("apple pie"), False)
    
    def test2(self):
        self.assertEqual(check_if_last_char_is_a_letter("apple pi e"), True)

    def test3(self):
        self.assertEqual(check_if_last_char_is_a_letter("apple pi e "), False)

    def test4(self):
        self.assertEqual(check_if_last_char_is_a_letter(""), False)

if __name__ == '__main__':
    unittest.main()