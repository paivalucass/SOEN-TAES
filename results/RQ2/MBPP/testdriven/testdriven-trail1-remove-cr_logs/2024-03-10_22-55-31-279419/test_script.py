def snake_to_camel(s):
    try:
        if not isinstance(s, str) or not s:
            raise ValueError("Input must be a non-empty string")
        return ''.join(word.capitalize() or '_' for word in s.split('_'))
    except ValueError as e:
        return str(e)
import unittest

class TestSnakeToCamel(unittest.TestCase):
    def test_snake_to_camel(self):
        self.assertEqual(snake_to_camel('python_program'), 'PythonProgram')

if __name__ == '__main__':
    unittest.main()