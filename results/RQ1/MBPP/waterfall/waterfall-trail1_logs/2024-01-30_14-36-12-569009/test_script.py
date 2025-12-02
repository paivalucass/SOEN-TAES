def replace_char(str1, ch, newch):
    if str1 and ch in str1:
        return str1.replace(ch, newch)
    else:
        return str1
    # Add input validation to check if the input string is not empty
    # Test cases should cover scenarios where the input string is empty, 
    # the character to be replaced is not present in the string, 
    # and the character to be replaced is present in the string.
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_char("polygon",'y','l'), "pollgon")

if __name__ == '__main__':
    unittest.main()