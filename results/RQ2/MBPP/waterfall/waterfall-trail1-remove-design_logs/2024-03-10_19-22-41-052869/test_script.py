def replace_spaces(text):
    return text.replace(' ', '_')
# Revised Code:
def replace_spaces_with_underscore(text):
    return text.replace(' ', '_')

assert replace_spaces_with_underscore('Jumanji The Jungle') == 'Jumanji_The_Jungle'
assert replace_spaces_with_underscore('Hello World') == 'Hello_World'
assert replace_spaces_with_underscore('Python is awesome') == 'Python_is_awesome'
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_spaces('Jumanji The Jungle'), 'Jumanji_The_Jungle')

if __name__ == '__main__':
    unittest.main()