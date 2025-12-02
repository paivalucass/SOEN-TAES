def string_to_list(string):
    if string is None or len(string) == 0:
        return []

    return string.split()
import unittest

class TestStringToList(unittest.TestCase):
    def test_string_to_list(self):
        self.assertEqual(string_to_list('python programming'), ['python', 'programming'])

if __name__ == '__main__':
    unittest.main()