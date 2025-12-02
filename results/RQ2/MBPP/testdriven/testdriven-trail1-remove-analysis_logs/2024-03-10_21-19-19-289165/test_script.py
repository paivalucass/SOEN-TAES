def parabola_directrix(a, b, c): 
    '''
    Write a function to find the directrix of a parabola.
    assert parabola_directrix(5,3,2)==-198
    '''

    # Calculate the directrix using the correct formula
    discriminant = b**2 - 4*a*c
    directrix = -discriminant / (4*a)
    return directrix

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(parabola_directrix(5, 3, 2), -198)

if __name__ == '__main__':
    unittest.main()