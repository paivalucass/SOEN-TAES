def remove_dirty_chars(input_string, dirty_chars):
    if not input_string or not dirty_chars:
        return "Invalid input"

    clean_string = ''.join(filter(lambda x: x not in dirty_chars, input_string))
    return clean_string
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_dirty_chars("probasscurve", "pros"), 'bacuve')

if __name__ == '__main__':
    unittest.main()