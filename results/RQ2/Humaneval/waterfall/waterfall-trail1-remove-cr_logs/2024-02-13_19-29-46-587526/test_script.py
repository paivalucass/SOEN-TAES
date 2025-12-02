from fractions import Fraction

def simplify(x, n):
    x_val = Fraction(x)
    n_val = Fraction(n)
    result = x_val * n_val
    return result == int(result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test('1/5', '5/1'), True)
        self.assertEqual(function_under_test('1/6', '2/1'), False)
        self.assertEqual(function_under_test('7/10', '10/2'), False)

if __name__ == '__main__':
    unittest.main()