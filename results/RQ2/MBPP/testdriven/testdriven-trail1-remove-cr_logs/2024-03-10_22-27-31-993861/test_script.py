def remove_dirty_chars(string, chars_to_remove):
    result = ''
    for char in string:
        if char not in chars_to_remove:
            result += char
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_dirty_chars("probasscurve", "pros"), 'bacuve')

if __name__ == '__main__':
    unittest.main()