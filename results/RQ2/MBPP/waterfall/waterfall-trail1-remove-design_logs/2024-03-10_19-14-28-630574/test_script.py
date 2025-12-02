def min_product_tuple(list1):
    if not isinstance(list1, list):
        raise ValueError("Input must be a list")
    for tup in list1:
        if not isinstance(tup, tuple) or len(tup) != 2:
            raise ValueError("Each element in the list must be a tuple containing exactly 2 values")
    
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