def string_to_list(string):
    if not isinstance(string, str):
        raise ValueError("Input must be a string")
    if string is None or len(string) == 0:
        return []
    return string.split()
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(string_to_list('python programming'), ['python', 'programming'])

if __name__ == '__main__':
    unittest.main()