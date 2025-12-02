def text_match_two_three(text):
    import re
    return bool(re.search(r'ab{2,3}', text))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_two_three('ac'), False)

if __name__ == '__main__':
    unittest.main()