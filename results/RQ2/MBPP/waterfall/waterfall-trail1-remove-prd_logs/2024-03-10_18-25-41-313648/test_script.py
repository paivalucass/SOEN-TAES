def remove_dirty_chars(original_string, dirty_chars):
    if not isinstance(original_string, str) or not isinstance(dirty_chars, str):
        return 'Invalid input: Both parameters should be strings.'
    
    if not original_string or not dirty_chars:
        return 'Invalid input: Both strings should not be empty.'
    
    clean_string = ''
    for char in original_string:
        if char.lower() not in dirty_chars.lower():
            clean_string += char
    
    return clean_string
import unittest

class Test(unittest.TestCase):
    def test_remove_dirty_chars(self):
        self.assertEqual(remove_dirty_chars("probasscurve", "pros"), 'bacuve')

if __name__ == '__main__':
    unittest.main()