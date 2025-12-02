import re

def replace_specialchar(text):
    return re.sub(r'[ ,.]', ':', text)

# Test the function
print(replace_specialchar('Python language, Programming language.'))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_specialchar('Python language, Programming language.'), 'Python:language::Programming:language:')

if __name__ == '__main__':
    unittest.main()