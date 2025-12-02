def replace_spaces(text):
    return text.replace(' ', '_')
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_spaces('Jumanji The Jungle'), 'Jumanji_The_Jungle')

if __name__ == '__main__':
    unittest.main()