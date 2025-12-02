def max_product_tuple(list1):
    try:
        if len(list1) == 0:
            return 0
        
        for tup in list1:
            if len(tup) != 2:
                return "Tuples inside the list are not of length 2"
                
            if not all(isinstance(num, (int, float)) for num in tup):
                return "Tuples inside the list contain non-numeric values or non-integer values"
        
        max_product = float('-inf')
        for tup in list1:
            product = abs(tup[0] * tup[1])
            if product > max_product:
                max_product = product
        
        return max_product
    
    except ValueError as ve:
        return str(ve)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]), 36)

if __name__ == '__main__':
    unittest.main()