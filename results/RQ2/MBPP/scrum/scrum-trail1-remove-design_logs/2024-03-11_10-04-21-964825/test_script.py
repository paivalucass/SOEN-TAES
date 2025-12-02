def snake_to_camel(word):
    if not word or "_" not in word:
        return word
    words = word.split("_")
    camel_word = words[0].capitalize() + ''.join([x.capitalize() for x in words[1:]])
    return camel_word
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(snake_to_camel('python_program'), 'PythonProgram')

if __name__ == '__main__':
    unittest.main()