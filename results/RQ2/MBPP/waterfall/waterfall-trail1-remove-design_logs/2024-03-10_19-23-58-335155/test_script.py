def replace_specialchar(text):
    import re
    return re.sub(r'[ ,.]', ':', text)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_specialchar('Python language, Programming language.'), 'Python:language::Programming:language:')

if __name__ == '__main__':
    unittest.main()