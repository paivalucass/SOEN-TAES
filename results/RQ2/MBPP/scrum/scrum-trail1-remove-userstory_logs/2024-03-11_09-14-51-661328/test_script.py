def toggle_string(string):
    return string.swapcase()
import unittest

class Test(unittest.TestCase):
    def test_toggle_string(self):
        self.assertEqual(toggle_string("Python"), "pYTHON")

if __name__ == '__main__':
    unittest.main()