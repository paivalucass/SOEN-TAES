def text_match_wordz_middle(text):
    def check_z_in_middle(word):
        middle_index = len(word) // 2
        if middle_index != 0 and middle_index != len(word) - 1 and word[middle_index] == 'z':
            return True
        else:
            return False

    if text:
        words = text.split()
        for word in words:
            if len(word) > 2 and check_z_in_middle(word):
                return True
        return False
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_wordz_middle('pythonzabc.'), True)

if __name__ == '__main__':
    unittest.main()