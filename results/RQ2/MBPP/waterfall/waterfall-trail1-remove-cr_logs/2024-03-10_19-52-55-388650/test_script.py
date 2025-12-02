def snake_to_camel(word):
    words = word.split('_')
    if any(not w.isalpha() for w in words):
        return "InvalidInputError"
    camel_case = words[0] + ''.join(w.title() for w in words[1:])
    return camel_case

assert snake_to_camel('python_program')=='PythonProgram'
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(snake_to_camel('python_program'), 'PythonProgram')

if __name__ == '__main__':
    unittest.main()