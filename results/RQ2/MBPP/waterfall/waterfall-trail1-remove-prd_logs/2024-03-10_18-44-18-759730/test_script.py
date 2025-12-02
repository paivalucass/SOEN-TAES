def move_num(test_str):
    if not test_str:
        raise ValueError("Input string is empty")
    
    if not test_str.isalnum():
        raise ValueError("Input string does not contain only alphanumeric characters")

    numbers = [char for char in test_str if char.isdigit()]
    non_numeric_chars = [char for char in test_str if not char.isdigit()]

    return ''.join(non_numeric_chars) + ''.join(numbers)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(move_num('I1love143you55three3000thousand'), 'Iloveyouthreethousand1143553000')

if __name__ == '__main__':
    unittest.main()