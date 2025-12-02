def toggle_string(string):
    if not string.isalpha():
        return "Error: Input should contain only alphabetic characters"
    
    toggled_case_string = string.swapcase()
    
    return toggled_case_string
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(toggle_string('Python'), 'pYTHON')

if __name__ == '__main__':
    unittest.main()