def text_match_one(text):
    import re
    return bool(re.search(r'a+b+', text))

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_one('ac'), False)

if __name__ == '__main__':
    unittest.main()