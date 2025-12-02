import unittest
import re

class TestStringMethods(unittest.TestCase):
    def test_text_match_zero_one(self):
        self.assertFalse(re.search(r'ab+', 'ac'))

if __name__ == '__main__':
    unittest.main()
import re

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_zero_one('ac'), False)

if __name__ == '__main__':
    unittest.main()