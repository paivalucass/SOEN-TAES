def int_to_mini_roman(number):
    if not 1 <= number <= 1000:
        return "Invalid input"
    
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]

    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]

    # Convert the number to mini roman numeral
    def convert_to_roman(num, val_list, syms_list):
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val_list[i]):
                roman_num += syms_list[i]
                num -= val_list[i]
            i += 1
        return roman_num.lower()

    return convert_to_roman(number, val, syms)
import unittest

class Test(unittest.TestCase):
    def test_int_to_mini_roman(self):
        self.assertEqual(int_to_mini_roman(19), 'xix')
        self.assertEqual(int_to_mini_roman(152), 'clii')
        self.assertEqual(int_to_mini_roman(426), 'cdxxvi')

if __name__ == '__main__':
    unittest.main()