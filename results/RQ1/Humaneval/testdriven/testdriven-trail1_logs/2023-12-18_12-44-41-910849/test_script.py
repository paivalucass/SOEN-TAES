def int_to_mini_roman(number):
    if number < 1 or number > 1000:
        raise ValueError("Input number must be within the range of 1 to 1000")

    roman_numerals = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }
    result = ''
    for value, numeral in roman_numerals.items():
        while number >= value:
            result += numeral
            number -= value
    return result.lower()
import unittest

class Test(unittest.TestCase):
    def test_int_to_mini_roman(self):
        self.assertEqual(int_to_mini_roman(19), 'xix')
        self.assertEqual(int_to_mini_roman(152), 'clii')
        self.assertEqual(int_to_mini_roman(426), 'cdxxvi')

if __name__ == '__main__':
    unittest.main()