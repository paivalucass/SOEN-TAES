def snake_to_camel(word):
    import re
    if not word:
        return ""
    return word.title().replace('_', '')
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(snake_to_camel('python_program'), 'PythonProgram')

if __name__ == '__main__':
    unittest.main()