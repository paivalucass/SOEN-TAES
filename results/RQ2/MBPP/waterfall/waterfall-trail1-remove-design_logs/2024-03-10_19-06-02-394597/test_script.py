def multiply_num(numbers):
    if not numbers:
        return "Error - Empty list input"
    
    total_product = 1
    for num in numbers:
        total_product *= num
    
    average_product = total_product / len(numbers)
    return average_product
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(multiply_num((8, 2, 3, -1, 7)), -67.2, delta=0.001)

if __name__ == '__main__':
    unittest.main()