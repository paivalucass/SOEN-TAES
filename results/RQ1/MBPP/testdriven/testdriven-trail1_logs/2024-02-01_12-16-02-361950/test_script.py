def replace_blank(input_string, replacement_char):
    if input_string is None or input_string == "":
        return ""
    else:
        return input_string.replace(' ', replacement_char)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_blank('hello people', '@'), "hello@people")

if __name__ == '__main__':
    unittest.main()