def min_product_tuple(list1):
    if len(list1) < 1:
        return None
    min_product = float('inf')
    for pair in list1:
        if len(pair) != 2 or type(pair[0]) != int or type(pair[1]) != int:
            return None
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