def replace_blank(str1, char):
    if not isinstance(str1, str) or not isinstance(char, str):
        raise TypeError("Input string and replacement character must be of type string")
    if not str1 or not char:
        raise ValueError("Input string and replacement character must not be empty")

    modified_string = str1.replace(" ", char)
    return modified_string
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_blank("hello people", '@'), "hello@people")

if __name__ == "__main__":
    unittest.main()