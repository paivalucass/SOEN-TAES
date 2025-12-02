def min_product_tuple(list_of_tuples):
    '''
    Write a function to find the minimum product from the pairs of tuples within a given list.
    assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==8
    '''
    if not list_of_tuples or len(list_of_tuples) < 2:
        return None
    
    min_product = None
    for tuple_pair in list_of_tuples:
        try:
            product = tuple_pair[0] * tuple_pair[1]
            if min_product is None or product < min_product:
                min_product = product
        except:
            pass
    
    return min_product
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]), 8)

if __name__ == '__main__':
    unittest.main()