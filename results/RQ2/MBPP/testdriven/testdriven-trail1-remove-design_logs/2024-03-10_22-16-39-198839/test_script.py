def replace_specialchar(text):
    if not isinstance(text, str) or text is None or text == '':
        return 'Invalid input data'
    
    return ':'.join(text.replace(' ', ':').replace(',', ':').replace('.', ':').split())
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_specialchar('Python language, Programming language.'), 'Python:language::Programming:language:')

if __name__ == '__main__':
    unittest.main()