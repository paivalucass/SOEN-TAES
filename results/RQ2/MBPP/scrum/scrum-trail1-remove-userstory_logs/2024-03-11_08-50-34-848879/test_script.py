def remove_dirty_chars(str1, str2):
    return ''.join([char for char in str1 if char not in str2])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_dirty_chars("probasscurve", "pros"), 'bacuve')

if __name__ == '__main__':
    unittest.main()