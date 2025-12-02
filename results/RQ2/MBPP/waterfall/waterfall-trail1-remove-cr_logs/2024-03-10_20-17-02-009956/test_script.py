def text_match_zero_one(text):
    import re
    return bool(re.search(r'ab+', text))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_zero_one('ac'), False)

if __name__ == '__main__':
    unittest.main()