def move_num(test_str):
    if not isinstance(test_str, str):
        return "Invalid input, please provide a string"
    
    alphabets = ""
    numbers = ""
    
    for char in test_str:
        if char.isalpha():
            alphabets += char
        elif char.isdigit():
            numbers += char
    
    return ''.join([alphabets, numbers])  # Using join method to concatenate alphabets and numbers

# Test the function
assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(move_num('I1love143you55three3000thousand'), 'Iloveyouthreethousand1143553000')

if __name__ == '__main__':
    unittest.main()