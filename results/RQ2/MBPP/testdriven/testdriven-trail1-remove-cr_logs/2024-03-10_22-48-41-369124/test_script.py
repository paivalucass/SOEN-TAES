def replace_spaces(string):
    if string is None or not isinstance(string, str):
        raise TypeError("Input should be a non-empty string")
    
    result = string.replace(" ", "%20")
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_spaces('My Name is Dawood'), 'My%20Name%20is%20Dawood')

if __name__ == '__main__':
    unittest.main()