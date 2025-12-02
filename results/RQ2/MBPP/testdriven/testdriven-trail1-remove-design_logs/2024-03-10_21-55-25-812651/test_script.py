def remove_dirty_chars(string, remove_chars):
    return string.translate({ord(char): None for char in remove_chars})
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_dirty_chars("probasscurve", "pros"), 'bacuve')

if __name__ == '__main__':
    unittest.main()