def toggle_string(string):
    if not isinstance(string, str):
        raise TypeError("Input should be a string")
    elif string == "":
        return ""
    else:
        return string.swapcase()
import unittest

class Test(unittest.TestCase):
    def test_toggle_string(self):
        self.assertEqual(toggle_string("Python"), "pYTHON")

if __name__ == '__main__':
    unittest.main()