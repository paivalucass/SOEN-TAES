def int_to_mini_roman(number):
    if not isinstance(number, int) or number < 1 or number > 1000:
        return "Invalid input"
    
    roman_dict = {
        1000: "m", 900: "cm", 500: "d", 400: "cd",
        100: "c", 90: "xc", 50: "l", 40: "xl",
        10: "x", 9: "ix", 5: "v", 4: "iv",
        1: "i"
    }
    
    roman_num = ''
    for val in roman_dict:
        while number >= val:
            roman_num += roman_dict[val]
            number -= val
    return roman_num.lower()
import unittest

class Test(unittest.TestCase):
    def test_int_to_mini_roman(self):
        self.assertEqual(int_to_mini_roman(19), 'xix')
        self.assertEqual(int_to_mini_roman(152), 'clii')
        self.assertEqual(int_to_mini_roman(426), 'cdxxvi')

if __name__ == '__main__':
    unittest.main()