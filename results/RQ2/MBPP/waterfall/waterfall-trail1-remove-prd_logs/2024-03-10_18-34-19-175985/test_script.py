def text_match_two_three(text):
    import re
    pattern = re.compile(r'a(b{2}|b{3})')
    return bool(pattern.search(text))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_two_three('ac'), False)

if __name__ == '__main__':
    unittest.main()