def simplify(x, n):
    def parse_fraction(fraction):
        numerator, denominator = map(int, fraction.split('/'))
        return numerator, denominator

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def simplify_fraction(fraction):
        numerator, denominator = fraction
        greatest_common_divisor = gcd(numerator, denominator)
        numerator //= greatest_common_divisor
        denominator //= greatest_common_divisor
        return numerator, denominator

    def multiply_fractions():
        numerator_x, denominator_x = parse_fraction(x)
        numerator_n, denominator_n = parse_fraction(n)
        result_numerator = numerator_x * numerator_n
        result_denominator = denominator_x * denominator_n
        result_fraction = (result_numerator, result_denominator)
        return result_fraction

    def is_whole_number(fraction):
        numerator, denominator = fraction
        return numerator % denominator == 0

    multiplied_fraction = multiply_fractions()
    simplified_fraction = simplify_fraction(multiplied_fraction)
    
    if simplified_fraction[1] > 999999999:
        return "Data Type Limitation"
    if simplified_fraction[1] == 0:
        return "Invalid Input"
    if is_whole_number(simplified_fraction):
        return True
    else:
        return False

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(simplify("1/5", "5/1"), True)
        self.assertEqual(simplify("1/6", "2/1"), False)
        self.assertEqual(simplify("7/10", "10/2"), False)

if __name__ == '__main__':
    unittest.main()