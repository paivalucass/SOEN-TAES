def remove_dirty_chars(input_string, chars_to_remove):
    modified_string = ''.join([char for char in input_string if char not in chars_to_remove])
    return modified_string
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_dirty_chars("probasscurve", "pros"), 'bacuve')

if __name__ == '__main__':
    unittest.main()