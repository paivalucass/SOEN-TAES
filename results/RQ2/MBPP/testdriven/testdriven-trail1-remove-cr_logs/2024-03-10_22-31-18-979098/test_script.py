def max_product_tuple(list1):
    if not list1:
        return 0  # Return 0 for empty input list

    max_product = float('-inf')  # Initialize max_product with negative infinity

    for pair in list1:
        if len(pair) < 2:
            continue  # Skip tuples with only one number

        product = abs(pair[0] * pair[1])  # Calculate the absolute product
        if product > max_product:
            max_product = product  # Update max_product if the current product is greater

    return max_product

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]), 36)

if __name__ == '__main__':
    unittest.main()