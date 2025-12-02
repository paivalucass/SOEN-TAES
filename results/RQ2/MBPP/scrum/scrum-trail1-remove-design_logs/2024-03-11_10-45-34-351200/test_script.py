def replace_char(str1, ch, newch):
    if not str1:
        return "Input string cannot be empty"
    
    if ch not in str1:
        return "Character to be replaced is not present in the input string"
    
    if len(ch) > 1 or len(newch) > 1:
        return "Only single characters can be replaced"

    return str1.replace(ch, newch)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_char('polygon', 'y', 'l'), 'pollgon')

if __name__ == '__main__':
    unittest.main()