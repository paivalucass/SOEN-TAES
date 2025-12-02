def toggle_string(string):
    if not isinstance(string, str):
        raise ValueError("Invalid input: input_string must be a string")

    result = ""
    for char in string:
        if char.isalpha():
            if char.islower():
                result += char.upper()
            else:
                result += char.lower()
        else:
            result += char

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(toggle_string('Python'), 'pYTHON')

if __name__ == '__main__':
    unittest.main()