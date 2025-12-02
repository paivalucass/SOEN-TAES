def min_product_tuple(list_of_tuples):
    if not list_of_tuples or any(len(t) != 2 for t in list_of_tuples):
        raise ValueError("Input list must not be empty and each tuple must contain exactly two elements")

    min_product = float('inf')
    for t in list_of_tuples:
        product = t[0] * t[1]
        min_product = min(min_product, product)

    return min_product

import unittest

class Test(unittest.TestCase):
    def test_min_product_tuple(self):
        self.assertEqual(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]), 8)

if __name__ == '__main__':
    unittest.main()