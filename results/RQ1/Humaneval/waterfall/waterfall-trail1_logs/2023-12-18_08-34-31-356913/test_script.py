def int_to_mini_roman(number):
    if not isinstance(number, int) or number <= 0 or number > 1000:
        raise ValueError("Input must be a positive integer between 1 and 1000")

    roman_numerals = {
        1000: "m", 900: "cm", 500: "d", 400: "cd",
        100: "c", 90: "xc", 50: "l", 40: "xl",
        10: "x", 9: "ix", 5: "v", 4: "iv",
        1: "i"
    }

    result = ""
    for value, numeral in roman_numerals.items():
        while number >= value:
            result += numeral
            number -= value
    return result
import unittest

class Test(unittest.TestCase):
    def test_int_to_mini_roman(self):
        self.assertEqual(int_to_mini_roman(19), 'xix')
        self.assertEqual(int_to_mini_roman(152), 'clii')
        self.assertEqual(int_to_mini_roman(426), 'cdxxvi')

if __name__ == '__main__':
    unittest.main()