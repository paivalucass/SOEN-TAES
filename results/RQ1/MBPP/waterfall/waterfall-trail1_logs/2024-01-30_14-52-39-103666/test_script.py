def is_upper(string):
  if not isinstance(string, str):
    return "Invalid input, please provide a string"
  return string.upper()
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_upper('person'), 'PERSON')

if __name__ == '__main__':
    unittest.main()