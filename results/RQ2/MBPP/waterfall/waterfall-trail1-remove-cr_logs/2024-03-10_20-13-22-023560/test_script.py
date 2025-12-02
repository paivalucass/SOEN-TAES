def replace_spaces(string):
    if not string or not ' ' in string:
        raise ValueError("Input string is empty or does not contain any spaces")
    
    result = ''
    for char in string:
        if char == ' ':
            result += '%20'
        else:
            result += char
    
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_spaces("My Name is Dawood"), 'My%20Name%20is%20Dawood')

if __name__ == '__main__':
    unittest.main()