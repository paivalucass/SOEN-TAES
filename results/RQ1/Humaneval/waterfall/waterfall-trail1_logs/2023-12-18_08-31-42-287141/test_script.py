def simplify(x, n):
    x_numerator, x_denominator = map(int, x.split('/'))
    n_numerator, n_denominator = map(int, n.split('/'))
    result = x_numerator * n_numerator / (x_denominator * n_denominator)
    return result.is_integer()
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(simplify("1/5", "5/1"), True)
        self.assertEqual(simplify("1/6", "2/1"), False)
        self.assertEqual(simplify("7/10", "10/2"), False)

if __name__ == '__main__':
    unittest.main()