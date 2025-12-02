def toggle_string(string):
    if not string:
        return "Error: Empty string"
    
    toggled_string = ""
    for char in string:
        if char.isalpha():
            if char.islower():
                toggled_string += char.upper()
            else:
                toggled_string += char.lower()
        else:
            toggled_string += char  # Convert non-alphabetic characters to the same character

    return toggled_string
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(toggle_string('Python'), 'pYTHON')

if __name__ == '__main__':
    unittest.main()