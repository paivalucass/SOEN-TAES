def simplify(x, n):
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))
    
    result_num = x_num * n_num
    result_den = x_den * n_den
    
    if result_num % result_den == 0:
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