def max_product_tuple(list1):
    if not list1:
        raise ValueError("Input list cannot be empty")
    
    for tuple_pair in list1:
        if len(tuple_pair) != 2:
            raise ValueError("Each tuple in the input list must contain exactly two elements")
        
    max_product = 0
    for tuple_pair in list1:
        product = abs(tuple_pair[0] * tuple_pair[1])
        max_product = max(max_product, product)
    return max_product
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]), 36)

if __name__ == '__main__':
    unittest.main()