def text_match_one(text):
    pattern = re.compile('ab+')
    return bool(pattern.search(text))
import re
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_one('ac'), False)

if __name__ == '__main__':
    unittest.main()