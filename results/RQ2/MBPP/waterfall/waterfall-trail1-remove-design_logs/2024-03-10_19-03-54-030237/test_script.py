def remove_dirty_chars(string, chars_to_remove):
    if string is None or not string:
        return ""

    translation_table = {ord(char): None for char in chars_to_remove}
    return string.translate(translation_table)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_dirty_chars("probasscurve", "pros"), 'bacuve')

if __name__ == '__main__':
    unittest.main()