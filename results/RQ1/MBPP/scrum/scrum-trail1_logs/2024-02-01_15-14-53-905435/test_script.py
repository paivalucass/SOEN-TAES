def text_match_two_three(text):
    import re
    pattern = r'a(b{2,3})'
    if re.fullmatch(pattern, text):
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_two_three('ac'), False)

if __name__ == '__main__':
    unittest.main()