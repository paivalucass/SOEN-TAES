def string_to_list(string):
    if not string:
        raise ValueError("Input string is empty")
    
    string = string.strip()
    if not string:
        raise ValueError("Input string has no non-space characters")

    return string.split()
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(string_to_list('python programming'), ['python', 'programming'])

if __name__ == '__main__':
    unittest.main()