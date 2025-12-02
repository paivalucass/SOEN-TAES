def string_to_list(string):
    if not isinstance(string, str):
        return "Error: Input must be a string"
    if not string:
        return []
    return string.split()
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(string_to_list('python programming'), ['python','programming'])

if __name__ == '__main__':
    unittest.main()