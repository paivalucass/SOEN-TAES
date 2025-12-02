def replace_char(original_string, old_char, new_char):
    if not original_string:
        return "Error: original_string is empty"
    
    if old_char not in original_string:
        return "Error: old_char not found in original_string"
    
    return original_string.replace(old_char, new_char)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_char("polygon", 'y', 'l'), "pollgon")

if __name__ == '__main__':
    unittest.main()