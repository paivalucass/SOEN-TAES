def parabola_directrix(a, b, c):
    '''
    Write a function to find the directrix of a parabola.
    assert parabola_directrix(5,3,2)==-198
    '''

    # Input validation
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        return "Input validation error message"

    # Error handling for zero value of 'a'
    if a == 0:
        return "Error message for invalid parabola equation"

    # Calculating directrix
    discriminant = b**2 - 4*a*c
    if discriminant < 0: 
        return "Error: The discriminant is negative, no real roots, and no directrix"
    directrix = -b / (2*a)
    return directrix
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(parabola_directrix(5, 3, 2), -198)

if __name__ == '__main__':
    unittest.main()