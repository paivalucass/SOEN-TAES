def max_product_tuple(list1):
    if not list1:
        raise ValueError("Input list cannot be empty")

    if len(list1) == 1:
        return abs(list1[0][0] * list1[0][1])

    for tuple in list1:
        if len(tuple) != 2:
            raise ValueError("Each tuple in the input list should contain exactly 2 numbers")

        if tuple[0] < 0 or tuple[1] < 0:
            raise ValueError("Input tuples cannot contain negative numbers")

    max_product = float('-inf')
    for pair in list1:
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