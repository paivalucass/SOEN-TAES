def convert(numbers):   
    # Write a python function to convert complex numbers to polar coordinates
    # assert convert(1) == (1.0, 0.0)
    import cmath
    
    def convert_to_polar_coordinates(complex_number):
        try:
            polar_coordinates = (abs(complex_number), cmath.phase(complex_number))
            return polar_coordinates
        except ValueError:
            return "Error: Invalid input, please provide a valid complex number."

    return convert_to_polar_coordinates(numbers)
import unittest

class Test(unittest.TestCase):
    def test_convert(self):
        self.assertEqual(convert(1), (1.0, 0.0))

if __name__ == '__main__':
    unittest.main()