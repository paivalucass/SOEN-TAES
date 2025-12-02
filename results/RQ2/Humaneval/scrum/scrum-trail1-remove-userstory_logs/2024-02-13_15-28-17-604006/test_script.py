def simplify(x, n):
    x_num, x_denom = map(int, x.split('/'))
    n_num, n_denom = map(int, n.split('/'))
    result_num = x_num * n_num
    result_denom = x_denom * n_denom
    if result_num % result_denom == 0:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test_simplify(self):
        self.assertEqual(simplify("1/5", "5/1"), True)
        self.assertEqual(simplify("1/6", "2/1"), False)
        self.assertEqual(simplify("7/10", "10/2"), False)

if __name__ == '__main__':
    unittest.main()