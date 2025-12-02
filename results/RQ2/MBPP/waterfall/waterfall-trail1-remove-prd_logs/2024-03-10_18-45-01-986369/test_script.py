def replace_spaces(text):
    if text is None or len(text) == 0:
        raise ValueError("Input text cannot be null or empty")

    modified_text = text.replace(' ', '_')
    modified_text = modified_text.replace('_', ' ')

    return modified_text
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_spaces('Jumanji The Jungle'), 'Jumanji_The_Jungle')

if __name__ == '__main__':
    unittest.main()