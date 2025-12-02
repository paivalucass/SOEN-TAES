def min_product_tuple(tuple_list):
    if len(tuple_list) == 0:
        return None

    min_product = float('inf')

    for tuple in tuple_list:
        if len(tuple) != 2:
            return "Invalid input: Each tuple should contain two elements"
        product = tuple[0] * tuple[1]
        if product < min_product:
            min_product = product

    return min_product
import unittest

class Test(unittest.TestCase):
    def test_min_product_tuple(self):
        self.assertEqual(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]), 8)

if __name__ == '__main__':
    unittest.main()