def capital_words_spaces(str1):
    import re
    return re.sub(r'(\w)([A-Z])', r'\1 \2', str1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(capital_words_spaces('Python'), 'Python')

if __name__ == '__main__':
    unittest.main()