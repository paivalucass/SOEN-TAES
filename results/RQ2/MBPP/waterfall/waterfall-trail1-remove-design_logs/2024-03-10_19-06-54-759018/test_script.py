def string_to_list(string):
    if not isinstance(string, str) or not string:
        raise ValueError('Input must be a non-empty string')
    
    return string.split(' ')
import unittest

class TestStringToList(unittest.TestCase):
    def test_string_to_list(self):
        self.assertEqual(string_to_list('python programming'), ['python', 'programming'])

if __name__ == '__main__':
    unittest.main()