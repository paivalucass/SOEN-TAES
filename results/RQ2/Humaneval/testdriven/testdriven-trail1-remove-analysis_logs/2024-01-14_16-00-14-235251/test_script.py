def simplify_fraction(fraction_str):
    numerator, denominator = map(int, fraction_str.split('/'))
    return numerator, denominator

def is_whole_number(result):
    return result % 1 == 0

def simplify(x, n):
    """
    Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """

    x_num, x_den = simplify_fraction(x)
    n_num, n_den = simplify_fraction(n)

    try:
        result = (x_num / x_den) * (n_num / n_den)
        return is_whole_number(result)
    except ZeroDivisionError:
        return "Error"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(simplify("1/5", "5/1"), True)
        self.assertEqual(simplify("1/6", "2/1"), False)
        self.assertEqual(simplify("7/10", "10/2"), False)

if __name__ == '__main__':
    unittest.main()