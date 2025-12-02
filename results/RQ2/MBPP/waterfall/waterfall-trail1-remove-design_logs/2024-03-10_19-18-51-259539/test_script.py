def toggle_string(string):
    if not isinstance(string, str) or not string.isalpha():
        return "Invalid input"
    
    return string.swapcase()
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(toggle_string('Python'), 'pYTHON')

if __name__ == '__main__':
    unittest.main()