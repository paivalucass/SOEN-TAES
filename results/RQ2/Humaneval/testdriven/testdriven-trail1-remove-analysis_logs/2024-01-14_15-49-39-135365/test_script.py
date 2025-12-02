def derivative(coefficients: list) -> list:
    """
    Calculate the derivative of a polynomial represented by its coefficients.
    
    Args:
    coefficients: list of coefficients of the polynomial
    
    Returns:
    List of coefficients representing the derivative of the polynomial
    """

    # Input validation
    if not isinstance(coefficients, list):
        raise TypeError("Input should be a list of coefficients")
    
    for coeff in coefficients:
        if not isinstance(coeff, (int, float)):
            raise TypeError("Coefficients should be numbers")
    
    # Derivative calculation
    derivative_coefficients = [coeff*i for i, coeff in enumerate(coefficients) if i > 0]

    return derivative_coefficients
import unittest

class Test(unittest.TestCase):
    def test_derivative_1(self):
        self.assertEqual(derivative([3, 1, 2, 4, 5]), [1, 4, 12, 20])

    def test_derivative_2(self):
        self.assertEqual(derivative([1, 2, 3]), [2, 6])

if __name__ == '__main__':
    unittest.main()