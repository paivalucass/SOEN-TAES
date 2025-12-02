def min_product_tuple(list1):
    if len(list1) % 2 != 0:
        return "Error: Input list does not contain pairs of numbers"

    min_product = float('inf')
    for pair in list1:
        product = pair[0] * pair[1]
        if product < min_product:
            min_product = product

    return min_product
import unittest

class Test(unittest.TestCase):
    def test_min_product_tuple(self):
        self.assertEqual(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]), 8)

if __name__ == '__main__':
    unittest.main()