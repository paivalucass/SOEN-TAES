def unique_product(list_data):
    # Input validation
    if not isinstance(list_data, list) or len(list_data) == 0:
        raise ValueError("Input list is empty or not a list")

    if not all(isinstance(x, (int, float)) for x in list_data):
        raise ValueError("Input list should contain only numbers")

    # Create a set of unique numbers
    unique_numbers = set(list_data)

    # Calculate the product of unique numbers
    product = 1
    for number in unique_numbers:
        product *= number

    return product
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(unique_product([10, 20, 30, 40, 20, 50, 60, 40]), 720000000)

if __name__ == '__main__':
    unittest.main()