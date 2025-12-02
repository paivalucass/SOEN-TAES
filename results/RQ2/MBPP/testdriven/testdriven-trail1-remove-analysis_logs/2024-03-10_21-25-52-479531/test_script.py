def replace_spaces(string):
    return string.replace(' ', '%20')

assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_spaces("My Name is Dawood"), 'My%20Name%20is%20Dawood')

if __name__ == '__main__':
    unittest.main()