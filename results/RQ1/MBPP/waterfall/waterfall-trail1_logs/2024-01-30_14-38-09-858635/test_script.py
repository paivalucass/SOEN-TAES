def toggle_string(string):
    if not isinstance(string, str) or len(string) == 0:
        return "Invalid input: input must be a non-empty string"

    toggled_string = string.swapcase()

    return toggled_string
import unittest

class Test(unittest.TestCase):
    def test_toggle_string(self):
        self.assertEqual(toggle_string("Python"), "pYTHON")

if __name__ == '__main__':
    unittest.main()