def max_product_tuple(list1):
    max_product = 0
    for tuple in list1:
        if len(tuple) != 2:
            raise ValueError("Each tuple in the input list must contain 2 elements")
        product = tuple[0] * tuple[1]
        if abs(product) > max_product:
            max_product = abs(product)
    return max_product
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]), 36)

if __name__ == '__main__':
    unittest.main()