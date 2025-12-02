def replace_specialchar(text):
    if text is None or len(text) == 0:
        return ""
    else:
        return text.replace(' ', ':').replace(',', ':').replace('.', ':')
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_specialchar('Python language, Programming language.'), 'Python:language::Programming:language:')

if __name__ == '__main__':
    unittest.main()