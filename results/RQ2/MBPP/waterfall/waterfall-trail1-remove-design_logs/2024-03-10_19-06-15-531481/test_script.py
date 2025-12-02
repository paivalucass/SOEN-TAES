def snake_to_camel(word):
    if not word:
        return ""
    
    parts = word.split('_')
    if len(parts) == 1:
        return word.title()
    
    return ''.join(x.title() for x in parts)
import unittest

class TestSnakeToCamel(unittest.TestCase):
    def test_snake_to_camel(self):
        self.assertEqual(snake_to_camel('python_program'), 'PythonProgram')

if __name__ == '__main__':
    unittest.main()