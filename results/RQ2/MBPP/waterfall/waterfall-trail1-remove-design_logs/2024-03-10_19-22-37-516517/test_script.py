def replace_spaces(string):
    import urllib.parse
    return urllib.parse.quote(string)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_spaces('My Name is Dawood'), 'My%20Name%20is%20Dawood')

if __name__ == '__main__':
    unittest.main()