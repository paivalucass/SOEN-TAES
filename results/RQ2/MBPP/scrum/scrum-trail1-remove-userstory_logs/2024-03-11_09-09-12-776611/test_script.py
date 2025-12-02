def calculate_tuple_product(tuple):
    result = 1
    for num in tuple:
        result *= num
    return result

def find_minimum_product(list_of_tuples):
    if not list_of_tuples:
        return None
    
    min_product = float('inf')
    for tuple in list_of_tuples:
        product = calculate_tuple_product(tuple)
        if product < min_product:
            min_product = product
    
    return min_product

def min_product_tuple(list1):
    return find_minimum_product(list1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]), 8)

if __name__ == '__main__':
    unittest.main()