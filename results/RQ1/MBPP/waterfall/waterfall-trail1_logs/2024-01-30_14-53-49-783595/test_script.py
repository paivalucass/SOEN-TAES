def replace_spaces(string):
    if not string.strip():  
        return ""

    modified_string = '%20'.join(string.split())
    return modified_string
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_spaces('My Name is Dawood'), 'My%20Name%20is%20Dawood')

if __name__ == '__main__':
    unittest.main()