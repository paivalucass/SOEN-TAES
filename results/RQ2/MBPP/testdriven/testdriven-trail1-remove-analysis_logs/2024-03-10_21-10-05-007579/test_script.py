def snake_to_camel(word):
    words_list = word.split('_')
    camel_case_string = ''.join([word.capitalize() for word in words_list])
    return camel_case_string
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(snake_to_camel('python_program'), 'PythonProgram')

if __name__ == '__main__':
    unittest.main()