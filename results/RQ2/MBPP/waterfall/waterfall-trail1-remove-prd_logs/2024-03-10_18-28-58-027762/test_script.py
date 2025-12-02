def string_to_list(string):
    if not string or not isinstance(string, str):
        return "Invalid input"
    else:
        return string.split()
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(string_to_list('python programming'), ['python', 'programming'])

if __name__ == '__main__':
    unittest.main()