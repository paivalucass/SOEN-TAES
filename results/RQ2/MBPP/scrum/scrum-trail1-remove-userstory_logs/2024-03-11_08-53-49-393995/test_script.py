def snake_to_camel(word):
    parts = word.split('_')
    return parts[0].capitalize() + ''.join(x.capitalize() or x for x in parts[1:])
import unittest

class Test(unittest.TestCase):
    def test_snake_to_camel(self):
        self.assertEqual(snake_to_camel('python_program'), 'PythonProgram')

if __name__ == '__main__':
    unittest.main()