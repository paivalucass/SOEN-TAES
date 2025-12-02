def replace_spaces(text):
    import re
    if not isinstance(text, str):
        return "Invalid input"
    if len(text) == 0:
        return text
    if len(text) > 1000000:
        return "Input text is too long"

    text = re.sub(r'\s', '_', text)
    
    return text
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_spaces('Jumanji The Jungle'), 'Jumanji_The_Jungle')

if __name__ == '__main__':
    unittest.main()