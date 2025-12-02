import re

def replace_spaces(text):
    if not isinstance(text, str):
        return "Error: Invalid input"

    if len(text) == 0:
        return ""

    result = re.sub(r'[ _]', '_', text)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_spaces('Jumanji The Jungle'), 'Jumanji_The_Jungle')

if __name__ == '__main__':
    unittest.main()