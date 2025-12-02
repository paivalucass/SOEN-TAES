def capital_words_spaces(str1):
    import re
    modified_string = re.sub(r"([a-z])([A-Z])", r"\1 \2", str1)
    return modified_string

assert capital_words_spaces("Python") == 'Python'
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(capital_words_spaces('Python'), 'Python')

if __name__ == '__main__':
    unittest.main()