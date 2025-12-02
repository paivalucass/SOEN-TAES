def max_product_tuple(list1):
    if len(list1) < 2:
        return 0
    
    max_product = 0
    for pair in list1:
        if not isinstance(pair, tuple) or len(pair) != 2:
            return "Error: Invalid input data type"
        
        product = abs(pair[0] * pair[1])
        if product > max_product:
            max_product = product
    
    return max_product
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]), 36)

if __name__ == '__main__':
    unittest.main()