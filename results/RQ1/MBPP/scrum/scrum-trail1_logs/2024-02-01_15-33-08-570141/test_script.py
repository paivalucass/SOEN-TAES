def min_product_tuple(list1):
    if not isinstance(list1, list):
        raise ValueError("Invalid Input Type Exception")

    if not all(isinstance(item, tuple) and len(item) == 2 for item in list1):
        raise ValueError("Input list should only contain tuples with two elements")

    if len(list1) < 2:
        raise ValueError("Input list should contain at least two tuples")

    min_product = float('inf')

    for pair in list1:
        product = pair[0] * pair[1]
        if product < min_product:
            min_product = product

    return min_product
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]), 8)

if __name__ == '__main__':
    unittest.main()