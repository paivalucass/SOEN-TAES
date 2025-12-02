def replace_spaces(text):
    if not isinstance(text, str) or not text:
        return "Error: Invalid input. Please provide a non-empty string."

    replaced_text = ""
    for char in text:
        if char == ' ':
            replaced_text += '_'
        elif char == '_':
            replaced_text += ' '
        else:
            replaced_text += char
    
    return replaced_text
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_spaces('Jumanji The Jungle'), 'Jumanji_The_Jungle')

if __name__ == '__main__':
    unittest.main()