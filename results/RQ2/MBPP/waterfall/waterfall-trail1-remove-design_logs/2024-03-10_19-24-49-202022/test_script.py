import re
def capital_words_spaces(str1):
    return re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', str1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(capital_words_spaces('Python'), 'Python')

if __name__ == '__main__':
    unittest.main()