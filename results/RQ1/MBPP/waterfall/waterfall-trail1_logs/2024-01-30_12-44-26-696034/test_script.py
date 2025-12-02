def replace_blank(str1, char):
    if str1 is None or len(str1) == 0:
        return "Input string is null or empty"
    
    for c in str1:
        if c != ' ' and not c.isalpha():
            return "Input string contains invalid characters"

    return str1.replace(' ', char)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_blank('hello people', '@'), 'hello@people')

if __name__ == '__main__':
    unittest.main()