def multiply(a, b):
    """
    Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """
    if type(a) != int or type(b) != int:
        return "Invalid input. Please input integers only."
    
    unit_digit_a = abs(a) % 10
    unit_digit_b = abs(b) % 10
    product = unit_digit_a * unit_digit_b
    return product
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(multiply(148, 412), 16)
        self.assertEqual(multiply(19, 28), 72)
        self.assertEqual(multiply(2020, 1851), 0)
        self.assertEqual(multiply(14,-15), 20)

if __name__ == '__main__':
    unittest.main()