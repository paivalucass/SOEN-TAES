def snake_to_camel(word):
    import re
    if not re.match('^[a-z]+(_[a-z]+)*$', word):
        raise ValueError("Input is not a valid snake case string")
    words = word.split('_')
    camel_case = words[0] + ''.join(word.title() for word in words[1:])
    return camel_case

assert snake_to_camel('python_program')=='PythonProgram'
import unittest

class TestSnakeToCamel(unittest.TestCase):

    def test_snake_to_camel(self):
        self.assertEqual(snake_to_camel('python_program'), 'PythonProgram')

if __name__ == '__main__':
    unittest.main()