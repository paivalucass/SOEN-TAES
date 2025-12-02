def replace_specialchar(text):
    '''Write a function to replace all occurrences of spaces, commas, or dots with a colon.'''
    # Implement the code to replace special characters with a colon using input validation and regular expressions
    # Return the modified text
    import re
    if not isinstance(text, str):
        return "Invalid input"
    
    # Replace special characters with a colon
    modified_text = re.sub(r'[ ,.]', ':', text)
    return modified_text
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_specialchar('Python language, Programming language.'), 'Python:language::Programming:language:')

if __name__ == '__main__':
    unittest.main()