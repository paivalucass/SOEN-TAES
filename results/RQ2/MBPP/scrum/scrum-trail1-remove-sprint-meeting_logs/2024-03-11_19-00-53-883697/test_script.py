def replace_spaces(string):
    if string is None or string.strip() == "":
        return ""
    modified_string = string.replace(" ", "%20")
    return modified_string
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_spaces("My Name is Dawood"), 'My%20Name%20is%20Dawood')

if __name__ == '__main__':
    unittest.main()