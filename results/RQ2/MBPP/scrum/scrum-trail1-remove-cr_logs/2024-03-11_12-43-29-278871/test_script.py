def max_product_tuple(list1):
    if not all(isinstance(item, tuple) and len(item) == 2 for item in list1):
        return "Error: Input list should only contain tuples with exactly two elements"
    
    absolute_products = [abs(x * y) for (x, y) in list1]
    max_product = max(absolute_products)
    
    return max_product
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]), 36)

if __name__ == '__main__':
    unittest.main()