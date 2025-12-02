def replace_blank(str1, char):
    if str1 == "" or char == "":
        return "Input string or character cannot be empty"
    
    result = ""
    for c in str1:
        if c == " ":
            result += char
        else:
            result += c
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_blank('hello people', '@'), 'hello@people')

if __name__ == '__main__':
    unittest.main()