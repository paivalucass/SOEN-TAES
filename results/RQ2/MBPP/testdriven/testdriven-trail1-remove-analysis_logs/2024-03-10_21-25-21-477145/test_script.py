def move_num(test_str):
    non_numeric_chars = []
    numeric_chars = []
    
    for char in test_str:
        if char.isdigit():
            numeric_chars.append(char)
        else:
            non_numeric_chars.append(char)
    
    return ''.join(non_numeric_chars) + ''.join(numeric_chars)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(move_num('I1love143you55three3000thousand'), 'Iloveyouthreethousand1143553000')

if __name__ == '__main__':
    unittest.main()