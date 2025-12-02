def simplify(x, n):
    from fractions import Fraction
    
    # Parse the string representations of fractions
    x_fraction = Fraction(x)
    n_fraction = Fraction(n)
    
    # Perform the multiplication
    result = x_fraction * n_fraction
    
    # Check if the result is a whole number
    if result == int(result):
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