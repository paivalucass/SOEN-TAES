def toggle_string(string):
    if not isinstance(string, str) or string is None:
        raise ValueError("Input is not a valid string")

    toggled_string = ""
    for char in string:
        if char.isalpha():
            if char.isupper():
                toggled_string += char.lower()
            else:
                toggled_string += char.upper()
        else:
            toggled_string += char

    return toggled_string
import unittest

class Test(unittest.TestCase):
    def test_toggle_string(self):
        self.assertEqual(toggle_string('Python'), 'pYTHON')

if __name__ == '__main__':
    unittest.main()