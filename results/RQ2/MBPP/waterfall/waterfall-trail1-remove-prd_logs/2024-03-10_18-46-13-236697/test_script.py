def replace_specialchar(text):
    if text is None or text == "":
        return "Error: Input string is empty or None."

    import re
    modified_text = re.sub(r'[ ,.]', ':', text)
    
    return modified_text
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_specialchar('Python language, Programming language.'), 'Python:language::Programming:language:')

if __name__ == '__main__':
    unittest.main()