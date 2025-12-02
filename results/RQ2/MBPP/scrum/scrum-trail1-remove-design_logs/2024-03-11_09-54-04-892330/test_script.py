def remove_dirty_chars(input_string, remove_string):
    return ''.join([char for char in input_string if char not in remove_string])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_dirty_chars("probasscurve", "pros"), 'bacuve')

if __name__ == '__main__':
    unittest.main()