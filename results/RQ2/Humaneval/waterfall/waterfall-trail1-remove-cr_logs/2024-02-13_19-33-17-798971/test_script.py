def simplify(x, n):
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))

    if x_den == 0 or n_den == 0:
        raise ValueError("Denominator cannot be zero")

    result = x_num * n_num / (x_den * n_den)

    return result == int(result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(simplify("1/5", "5/1"), True)
        self.assertEqual(simplify("1/6", "2/1"), False)
        self.assertEqual(simplify("7/10", "10/2"), False)

if __name__ == '__main__':
    unittest.main()