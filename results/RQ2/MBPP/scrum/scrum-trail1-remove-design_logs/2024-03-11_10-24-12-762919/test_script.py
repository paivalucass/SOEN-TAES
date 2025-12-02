def text_match_two_three(text):
    import re
    pattern = 'ab{2,3}'
    if isinstance(text, str) and len(text) > 0:
        return bool(re.search(pattern, text))
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_two_three('ac'), False)

if __name__ == '__main__':
    unittest.main()