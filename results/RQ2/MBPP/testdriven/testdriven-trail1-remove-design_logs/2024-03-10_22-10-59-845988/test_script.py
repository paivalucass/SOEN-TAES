def toggle_string(string):
    if not isinstance(string, str):
        return "Error: Input is not a string"

    toggled_string = ""
    for char in string:
        if char.islower():
            toggled_string += char.upper()
        elif char.isupper():
            toggled_string += char.lower()
        else:
            toggled_string += char

    return toggled_string
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(toggle_string('Python'), 'pYTHON')

if __name__ == '__main__':
    unittest.main()