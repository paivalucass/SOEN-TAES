def replace_specialchar(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    special_chars = [' ', ',', '.']
    for char in special_chars:
        text = text.replace(char, ':')

    return text
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_specialchar('Python language, Programming language.'), 'Python:language::Programming:language:')

if __name__ == '__main__':
    unittest.main()