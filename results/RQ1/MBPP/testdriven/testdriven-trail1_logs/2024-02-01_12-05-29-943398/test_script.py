def max_product_tuple(list1: list[tuple[int, int]]) -> int:
    if not list1 or any(len(t) != 2 for t in list1):
        return "Invalid input"
    
    max_product = 0
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