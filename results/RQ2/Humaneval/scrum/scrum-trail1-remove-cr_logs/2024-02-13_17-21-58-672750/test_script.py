def int_to_mini_roman(number):
    if not isinstance(number, int) or number < 1 or number > 1000:
        raise ValueError("Input must be a positive integer within the range of 1 to 1000")
    
    roman_mapping = {
        1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'xc',
        100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'
    }
    
    result = ''
    for value, numeral in sorted(roman_mapping.items(), reverse=True):
        while number >= value:
            result += numeral
            number -= value
    
    return result.lower()
import unittest

class Test(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(int_to_mini_roman(19), 'xix')

    def test_case_2(self):
        self.assertEqual(int_to_mini_roman(152), 'clii')

    def test_case_3(self):
        self.assertEqual(int_to_mini_roman(426), 'cdxxvi')

if __name__ == '__main__':
    unittest.main()