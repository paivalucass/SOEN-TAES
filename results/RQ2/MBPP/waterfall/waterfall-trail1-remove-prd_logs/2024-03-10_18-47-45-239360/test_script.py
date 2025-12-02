def text_match_zero_one(text):
    import re
    pattern = r"ab+"
    if re.match(pattern, text):
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_zero_one('ac'), False)

if __name__ == '__main__':
    unittest.main()