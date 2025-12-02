def babylonian_squareroot(number):
    '''This function computes square roots using the babylonian method.'''
    assert isinstance(number, (int, float)), "Error: Invalid input"
    assert number >= 0, "Error: Invalid input"
    
    if number == 0:
        return 0.0

    x = number
    y = 1
    e = 0.000001
    while x - y > e:
        x = (x + y) / 2
        y = number / x
    return round(x, 15)
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(babylonian_squareroot(10), 3.162277660168379, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()