def replace_spaces(text):
    if not isinstance(text, str):
        raise ValueError('Input text must be a valid string')
    
    if not text.strip():
        return text
    
    modified_text = ''
    for char in text:
        if char == ' ':
            modified_text += '_'
        elif char == '_':
            modified_text += ' '
        else:
            modified_text += char
    
    return modified_text
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_spaces('Jumanji The Jungle'), 'Jumanji_The_Jungle')

if __name__ == '__main__':
    unittest.main()