def convert(numbers):
    '''
    Write a python function to convert complex numbers to polar coordinates.
    assert convert(1) == (1.0, 0.0)
    '''

    import cmath

    if isinstance(numbers, (int, float)):
        polar = (abs(numbers), cmath.phase(numbers))
    else:
        polar = [(abs(number), cmath.phase(number)) for number in numbers]
    
    return polar
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(convert(1), (1.0, 0.0))

if __name__ == '__main__':
    unittest.main()