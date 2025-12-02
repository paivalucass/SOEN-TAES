def replace_spaces(text):
    result = ''.join(['_' if char == ' ' else ' ' if char == '_' else char for char in text])
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_spaces('Jumanji The Jungle'), 'Jumanji_The_Jungle')

if __name__ == '__main__':
    unittest.main()