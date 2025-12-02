def snake_to_camel(word):
    if not word or all([char == '_' for char in word]):
        raise ValueError("Input word cannot be empty or contain only underscores")

    words = word.split('_')

    camel_case_word = words[0] + ''.join([word.capitalize() for word in words[1:]])

    return camel_case_word
import unittest

class TestSnakeToCamel(unittest.TestCase):
    def test_snake_to_camel(self):
        self.assertEqual(snake_to_camel('python_program'), 'PythonProgram')

if __name__ == '__main__':
    unittest.main()