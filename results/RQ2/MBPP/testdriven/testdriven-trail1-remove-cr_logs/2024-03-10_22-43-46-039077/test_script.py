def replace_char(str1, ch, newch):
    if ch not in str1:
        return "Specified character not found in the input string"
    
    if str1.count(ch) > 1:
        return "Specified character occurs multiple times in the input string"
    
    new_string = str1.replace(ch, newch)
    
    return new_string
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_char("polygon", 'y', 'l'), "pollgon")

if __name__ == '__main__':
    unittest.main()