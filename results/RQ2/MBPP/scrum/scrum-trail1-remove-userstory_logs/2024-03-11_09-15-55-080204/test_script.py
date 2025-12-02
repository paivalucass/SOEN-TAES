from typing import List

def unique_product(list_data: List[float]) -> float:
    # Create a set to store unique numbers from the input list
    unique_numbers = set(list_data)
    
    # Calculate the product of the unique numbers in the set
    product = 1
    for number in unique_numbers:
        product *= number
    
    # Return the product of the unique numbers
    return product
import unittest

class Test(unittest.TestCase):
    def test_unique_product(self):
        self.assertEqual(unique_product([10, 20, 30, 40, 20, 50, 60, 40]), 720000000)

if __name__ == '__main__':
    unittest.main()