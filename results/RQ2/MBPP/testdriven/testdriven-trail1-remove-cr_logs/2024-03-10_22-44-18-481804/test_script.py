def toggle_string(string):
    if not isinstance(string, str):
        return "Invalid input"
    toggled_string = ""
    for char in string:
        if char.isalpha():
            if char.islower():
                toggled_string += char.upper()
            else:
                toggled_string += char.lower()
        else:
            toggled_string += char
    return toggled_string

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(toggle_string("Python"), "pYTHON")
        self.assertEqual(toggle_string("hello WORLD"), "HELLO world")
        self.assertEqual(toggle_string(""), "")

if __name__ == '__main__':
    unittest.main()