def unique_product(list_data):
    if not isinstance(list_data, list):
        raise TypeError("Input must be a list of numbers")

    if len(list_data) == 0:
        raise ValueError("Input list cannot be empty")

    unique_numbers = set(list_data)
    product = 1
    for num in unique_numbers:
        if num < 0:
            raise ValueError("Input list cannot contain negative numbers")
        product *= num
    return product
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(unique_product([10, 20, 30, 40, 20, 50, 60, 40]), 720000000)

if __name__ == '__main__':
    unittest.main()