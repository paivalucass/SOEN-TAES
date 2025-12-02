def replace_spaces(string):
    if not string:
        raise ValueError("Input string cannot be empty")
    
    string = string.strip()
    
    string = string.replace(" ", "%20")
    
    return string
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_spaces('My Name is Dawood'), 'My%20Name%20is%20Dawood')

if __name__ == '__main__':
    unittest.main()