def int_to_mini_roman(number):
    roman_numerals = {
        1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l',
        90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'
    }

    if not isinstance(number, int) or number < 1 or number > 1000:
        raise ValueError("Input must be a positive integer within the range of 1 to 1000")

    result = ''
    for value in sorted(roman_numerals.keys(), reverse=True):
        while number >= value:
            result += roman_numerals[value]
            number -= value

    return result.lower()
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(int_to_mini_roman(19), 'xix')
        self.assertEqual(int_to_mini_roman(152), 'clii')
        self.assertEqual(int_to_mini_roman(426), 'cdxxvi')

if __name__ == '__main__':
    unittest.main()