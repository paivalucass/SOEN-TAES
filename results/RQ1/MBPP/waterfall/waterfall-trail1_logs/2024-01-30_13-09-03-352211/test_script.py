def min_product_tuple(list1):
    if not list1:
        raise ValueError("Input list is empty")
    
    for tup in list1:
        if len(tup) != 2:
            raise ValueError("Each tuple in the input list must contain exactly two elements")
    
    min_product = float('inf')
    
    for tup in list1:
        product = tup[0] * tup[1]
        if product < min_product:
            min_product = product
    
    return min_product
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]), 8)

if __name__ == '__main__':
    unittest.main()