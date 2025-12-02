def snake_to_camel(word):
    word_list = word.split('_')
    camel_word = word_list[0].capitalize() + ''.join([x.capitalize() for x in word_list[1:]])
    return camel_word
import unittest

class TestSnakeToCamel(unittest.TestCase):
    def test_snake_to_camel(self):
        self.assertEqual(snake_to_camel('python_program'), 'PythonProgram')

if __name__ == '__main__':
    unittest.main()