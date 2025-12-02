def snake_to_camel(word):
  words = word.split('_')
  return ''.join([w.title() for w in words])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(snake_to_camel('python_program'), 'PythonProgram')

if __name__ == '__main__':
    unittest.main()