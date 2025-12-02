def remove_dirty_chars(input_string, chars_to_remove):
    if not isinstance(input_string, str) or not isinstance(chars_to_remove, str):
        raise TypeError("Input parameters are of incorrect data type")
    
    result = ''.join([char for char in input_string if char not in chars_to_remove])
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_dirty_chars('probasscurve', 'pros'), 'bacuve')

if __name__ == '__main__':
    unittest.main()