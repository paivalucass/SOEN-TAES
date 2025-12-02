def replace_blank(str1, char):
    if str1 is None:
        return "Error: Null value input"
    elif not isinstance(str1, str) or not isinstance(char, str):
        return "Error: Invalid input value"
    else:
        return str1.replace(" ", char)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_blank("hello people", '@'), "hello@people")

if __name__ == '__main__':
    unittest.main()